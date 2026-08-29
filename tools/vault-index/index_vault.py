#!/usr/bin/env python3
"""
Vault semantic indexer — embeds Obsidian notes into Qdrant using fastembed.

Runs incrementally: only re-indexes notes that have changed since the last run.
State is tracked in ~/.local/share/vault-index/state.json.

Usage:
    python index_vault.py [--full]   # --full forces re-index of everything
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from fastembed import TextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

# ── Config ────────────────────────────────────────────────────────────────────

VAULT_PATH  = Path("~/vault").expanduser()   # ← set to your vault root
QDRANT_URL  = "http://localhost:6333"
STATE_FILE  = Path.home() / ".local/share/vault-index/state.json"
COLLECTION  = "vault"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_SIZE = 384    # all-MiniLM-L6-v2 output dimension
VECTOR_NAME = "fast-all-minilm-l6-v2"  # must match mcp-server-qdrant's get_vector_name()

# Folders to index (adjust to match your vault structure)
INCLUDE_FOLDERS = [
    "10 - Projects",
    "20 - Areas",
    "30 - Resources",
    "35 - Techniques",
]
EXCLUDE_FOLDERS = {"_resources", "90 - Templates", ".git"}
EXCLUDE_FILES   = {"README.md"}

_embedder: TextEmbedding | None = None

def get_embedder() -> TextEmbedding:
    global _embedder
    if _embedder is None:
        _embedder = TextEmbedding(model_name=EMBED_MODEL)
    return _embedder


# ── Helpers ───────────────────────────────────────────────────────────────────

def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text). Frontmatter is optional."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[4:end]
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_block.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, body


def build_text_for_embedding(path: Path, fm: dict, body: str) -> str:
    """Compose what we actually embed: path context + key frontmatter + body."""
    parts = [f"File: {path.relative_to(VAULT_PATH)}"]
    for key in ("title", "type", "tags", "status"):
        if key in fm:
            parts.append(f"{key}: {fm[key]}")
    parts.append(body[:4000])
    return "\n".join(parts)


def embed(text: str) -> list[float]:
    return list(next(get_embedder().embed([text])))


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def note_id(path: Path) -> str:
    return str(path.relative_to(VAULT_PATH))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="Re-index everything")
    args = parser.parse_args()

    client = QdrantClient(url=QDRANT_URL)

    existing = {c.name for c in client.get_collections().collections}
    if COLLECTION not in existing:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config={VECTOR_NAME: VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)},
        )
        print(f"Created collection '{COLLECTION}'")

    state = {} if args.full else load_state()
    indexed = updated = skipped = errors = 0

    candidates: list[Path] = []
    for folder in INCLUDE_FOLDERS:
        folder_path = VAULT_PATH / folder
        if not folder_path.exists():
            continue
        for path in folder_path.rglob("*.md"):
            if any(ex in path.parts for ex in EXCLUDE_FOLDERS):
                continue
            if path.name in EXCLUDE_FILES:
                continue
            candidates.append(path)

    print(f"Found {len(candidates)} notes to check")

    points: list[PointStruct] = []
    new_state: dict = dict(state)

    for path in candidates:
        nid = note_id(path)
        h = file_hash(path)

        if not args.full and state.get(nid) == h:
            skipped += 1
            continue

        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            fm, body = extract_frontmatter(text)
            embed_text = build_text_for_embedding(path, fm, body)
            vector = embed(embed_text)

            point_id = int(hashlib.md5(nid.encode()).hexdigest()[:8], 16)

            points.append(PointStruct(
                id=point_id,
                vector={VECTOR_NAME: vector},
                payload={
                    "document": embed_text,   # required by mcp-server-qdrant
                    "metadata": {             # surfaced as entry.metadata in search results
                        "path": nid,
                        "title": fm.get("title", path.stem),
                        "type": fm.get("type", ""),
                        "status": fm.get("status", ""),
                        "tags": fm.get("tags", ""),
                        "folder": str(path.parent.relative_to(VAULT_PATH)),
                        "indexed_at": datetime.now(timezone.utc).isoformat(),
                    },
                },
            ))
            new_state[nid] = h

            if state.get(nid):
                updated += 1
                print(f"  updated: {nid}")
            else:
                indexed += 1
                print(f"  indexed: {nid}")

            if len(points) >= 20:
                client.upsert(collection_name=COLLECTION, points=points)
                points = []

        except Exception as e:
            errors += 1
            print(f"  ERROR {nid}: {e}", file=sys.stderr)

    if points:
        client.upsert(collection_name=COLLECTION, points=points)

    save_state(new_state)

    total = client.count(collection_name=COLLECTION).count
    print(f"\nDone — {indexed} new, {updated} updated, {skipped} unchanged, {errors} errors")
    print(f"Collection total: {total} notes")


if __name__ == "__main__":
    main()
