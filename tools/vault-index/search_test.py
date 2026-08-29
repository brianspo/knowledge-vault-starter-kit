#!/usr/bin/env python3
"""Quick search test — run this to verify the index works before wiring up the MCP."""
import sys
from fastembed import TextEmbedding
from qdrant_client import QdrantClient

QDRANT_URL  = "http://localhost:6333"
COLLECTION  = "vault"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_NAME = "fast-all-minilm-l6-v2"

query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "project status update"

client = QdrantClient(url=QDRANT_URL)
embedder = TextEmbedding(model_name=EMBED_MODEL)
vector = list(next(embedder.embed([query])))

results = client.query_points(
    collection_name=COLLECTION,
    query=vector,
    using=VECTOR_NAME,
    limit=5,
    with_payload=True,
).points

print(f"Query: {query!r}\n")
for i, r in enumerate(results, 1):
    m = r.payload.get("metadata", r.payload)
    print(f"{i}. [{r.score:.3f}] {m['path']}")
    print(f"   type={m['type']} status={m['status']} tags={m['tags']}")
