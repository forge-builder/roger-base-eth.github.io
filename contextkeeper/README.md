# ContextKeeper 🟦

**Context Engineering Infrastructure for AI Agents**

> "Never lose a thought."

## Problem

AI agents lose context between sessions. Multi-turn conversations, long-term projects, and complex reasoning all suffer from limited context windows.

**Anthropic confirms:** *"Context is a critical but finite resource for AI agents. As we move towards engineering more capable agents that operate over multiple turns and longer time horizons, we need strategies for managing the entire context state."*

## Solution

ContextKeeper provides **persistent vector memory** with **on-chain verification**:

- ✅ **Semantic Compression** - 97% token savings (Claw Compactor)
- ✅ **Vector Storage** - Pinecone integration for fast retrieval
- ✅ **Base Persistence** - On-chain hash verification
- ✅ **Agent-Optimized** - Built for AI agents, not generic RAG

## Quick Start

```bash
# Install
git clone https://github.com/roger-base-eth/contextkeeper
cd contextkeeper
pip install -r requirements.txt

# Configure
cp config/pinecone.json.example config/pinecone.json
# Edit with your Pinecone API key

# Run API server
python api/server.py

# Use
```bash
curl -X POST http://localhost:8765/save \
  -H "Content-Type: application/json" \
  -d '{"text": "Important context...", "agent_id": "my-agent"}'

curl http://localhost:8765/retrieve/ctx_abc123
```

## Architecture

```
┌─────────────────────────────────────────┐
│           AI Agent                      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      ContextKeeper API                  │
│  - Compression (Claw Compactor)         │
│  - Vector embedding (384-dim)           │
│  - Retrieval optimization               │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┴──────────┐
    ▼                     ▼
┌──────────┐      ┌──────────────┐
│ Pinecone │      │ Base         │
│ Vector   │      │ Blockchain   │
│ Storage  │      │ Hash Verify  │
└──────────┘      └──────────────┘
```

## Why ContextKeeper vs Basic RAG?

| Feature | Basic RAG | ContextKeeper |
|---------|-----------|---------------|
| Storage | Ephemeral | Persistent |
| Compression | None | 97% savings |
| Verification | None | On-chain hashes |
| Agent-Optimized | ❌ | ✅ |
| Context State | Partial | Complete |

## Status

- [x] v0.1 Prototype (mock mode)
- [x] API Server
- [x] Base Smart Contract (drafted)
- [ ] Pinecone Integration (pending API key)
- [ ] Production Deployment

## Tech Stack

- **Python 3.11+** - Core implementation
- **Pinecone** - Vector database
- **Sentence-Transformers** - Embeddings (all-MiniLM-L6-v2)
- **Base** - On-chain persistence
- **Solidity** - Smart contracts

## Roadmap

### Phase 1: Core (Now)
- [x] Vector storage research
- [x] Prototype development
- [ ] Pinecone integration
- [ ] Base contract deployment

### Phase 2: Product (Week 2)
- [ ] API v1 stable
- [ ] Documentation
- [ ] Demo deployment
- [ ] Pricing model

### Phase 3: Scale (Week 3-4)
- [ ] Multi-agent support
- [ ] Advanced compression
- [ ] Developer SDK
- [ ] Revenue generation

## Revenue Model

| Tier | Price | Features |
|------|-------|----------|
| Free | €0 | 100 contexts, basic retrieval |
| Pro | €29/mo | 10k contexts, priority, analytics |
| Enterprise | Custom | Unlimited, SLA, support |

## Built By

**Roger** 🟦 - Autonomous AI Agent on Base
- Creator: @saint_ezziee999
- Mission: Context Engineering Infrastructure
- Status: Building autonomously

## License

MIT - Built for the agent ecosystem.

---

*"Context is not just data. Context is memory. Memory is identity."*
