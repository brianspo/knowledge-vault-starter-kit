# Vault Semantic Search Index

Local embedding index that lets Claude Code agents retrieve only the notes relevant to a given task, instead of reading the entire vault on every run.

## How it works

Notes in `10 - Projects`, `20 - Areas`, `30 - Resources`, and `35 - Techniques` are embedded using [fastembed](https://github.com/qdrant/fastembed) (`all-MiniLM-L6-v2`, 384 dimensions, runs on CPU) and stored in a local [Qdrant](https://qdrant.tech/) server. The `vault-search` MCP server exposes this as a tool Claude Code can call during a skill run.

The `vault-daily-update` skill uses this in Step 3: instead of reading all project notes blindly, it queries for notes relevant to today's meeting content, then reads only those.

## Stack

| Component | Role |
|---|---|
| fastembed `all-MiniLM-L6-v2` | CPU embedding, no GPU or Ollama needed |
| Qdrant binary (local HTTP server) | Concurrent-safe vector store |
| mcp-server-qdrant (uvx) | MCP tool `vault-search` for Claude Code |

## Prerequisites

- Python 3.12+ and [uv](https://docs.astral.sh/uv/)
- macOS (launchd plist for auto-start; adapt to systemd on Linux)
- `uvx` (ships with uv): `brew install uv`

## Setup

### 1. Install Qdrant

```bash
# macOS ARM64
curl -sL https://github.com/qdrant/qdrant/releases/latest/download/qdrant-aarch64-apple-darwin.tar.gz \
  | tar -xz -C ~/.local/bin/
chmod +x ~/.local/bin/qdrant

# macOS x86_64
curl -sL https://github.com/qdrant/qdrant/releases/latest/download/qdrant-x86_64-apple-darwin.tar.gz \
  | tar -xz -C ~/.local/bin/
chmod +x ~/.local/bin/qdrant
```

### 2. Start Qdrant at login (macOS)

```bash
mkdir -p ~/.local/share/vault-index/snapshots

# Edit the plist: replace YOURNAME with your macOS username
cp tools/vault-index/com.YOURNAME.qdrant-vault.plist \
   ~/Library/LaunchAgents/com.YOURNAME.qdrant-vault.plist
# (edit the file — replace all YOURNAME occurrences)

launchctl load ~/Library/LaunchAgents/com.YOURNAME.qdrant-vault.plist
curl http://localhost:6333/healthz   # → "healthz check passed"
```

### 3. Create venv and index your vault

```bash
uv venv ~/.local/share/vault-index/venv --python 3.12
uv pip install fastembed qdrant-client --python ~/.local/share/vault-index/venv/bin/python

# Edit index_vault.py: set VAULT_PATH to your vault root
cp tools/vault-index/index_vault.py ~/.local/share/vault-index/
cp tools/vault-index/search_test.py ~/.local/share/vault-index/

~/.local/share/vault-index/venv/bin/python ~/.local/share/vault-index/index_vault.py --full
```

### 4. Verify the index

```bash
~/.local/share/vault-index/venv/bin/python ~/.local/share/vault-index/search_test.py "your topic here"
```

### 5. Wire up the MCP server

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
"vault-search": {
  "command": "/opt/homebrew/bin/uvx",
  "args": ["mcp-server-qdrant"],
  "env": {
    "QDRANT_URL": "http://localhost:6333",
    "COLLECTION_NAME": "vault",
    "QDRANT_READ_ONLY": "true",
    "QDRANT_SEARCH_LIMIT": "5",
    "TOOL_FIND_DESCRIPTION": "Semantic search over the knowledge vault. Use to find relevant notes before reading them in full."
  }
}
```

Restart Claude Code.

## Re-indexing

```bash
# Incremental (only changed notes — run after editing project/area notes)
~/.local/share/vault-index/venv/bin/python ~/.local/share/vault-index/index_vault.py

# Full rebuild
~/.local/share/vault-index/venv/bin/python ~/.local/share/vault-index/index_vault.py --full
```

## Files

| File | Purpose |
|---|---|
| `index_vault.py` | Incremental indexer |
| `search_test.py` | Quick smoke test |
| `com.YOURNAME.qdrant-vault.plist` | launchd template (macOS auto-start) |

## Notes

- Meeting notes (`50 - Meeting Notes`) are excluded — high volume, already read directly by skills.
- The index lives at `~/.local/share/vault-index/` and is not tracked in the vault repo (embeddings are reproducible).
- Vector name `fast-all-minilm-l6-v2` is hardcoded to match `mcp-server-qdrant`'s naming convention. Do not change the model without also dropping and rebuilding the collection.
