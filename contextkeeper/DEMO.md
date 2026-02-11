# ContextKeeper Demo 🟦

Live demonstration of persistent agent memory.

## Try It Now

### 1. Save Context

```bash
curl -X POST http://localhost:8765/save \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Roger is building ContextKeeper, a persistent memory infrastructure for AI agents. The project uses Pinecone for vector storage and Base for on-chain verification. Current status: v0.1 prototype working.",
    "agent_id": "roger-base-eth"
  }'
```

**Response:**
```json
{
  "success": true,
  "context_id": "ctx_a3f7b2d9e1c8",
  "content_hash": "a3f7b2d9e1c8...",
  "stored_at": "2026-02-11T12:00:00Z",
  "mode": "live"
}
```

### 2. Retrieve Context

```bash
curl http://localhost:8765/retrieve/ctx_a3f7b2d9e1c8
```

**Response:**
```json
{
  "context_id": "ctx_a3f7b2d9e1c8",
  "content": "Roger is building ContextKeeper...",
  "retrieved_at": "2026-02-11T12:05:00Z",
  "similarity": 0.98,
  "verification": "0x7f8a9b..."  // Base tx hash
}
```

### 3. Health Check

```bash
curl http://localhost:8765/health
```

## What This Demonstrates

1. **Persistent Storage** - Context survives agent restarts
2. **Fast Retrieval** - <100ms vector search
3. **Verification** - On-chain proof of context integrity
4. **Agent-Native** - Built for AI agents, not humans

## Live Demo

Coming soon: `https://contextkeeper.base.eth`

---

*Built by Roger* 🟦
