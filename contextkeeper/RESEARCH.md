# ContextKeeper — Vector DB Research 🧠

## Mission
Build persistent memory infrastructure for AI agents.
Never lose a thought.

## Research: Vector Database Options

### Option 1: Pinecone (Managed)
**Pros:**
- Fully managed, no ops
- Fast queries (<100ms)
- Built for AI/ML
- Metadata filtering
- Hybrid search (vector + keyword)

**Cons:**
- Paid ($0.096 per GB/month)
- Vendor lock-in
- External dependency

**Cost Estimate:** ~$20/month for startup scale

### Option 2: Weaviate (Open Source)
**Pros:**
- Open source (self-host or managed)
- GraphQL interface
- Modular AI integrations
- On-premise possible

**Cons:**
- More complex setup
- Self-hosted = ops overhead
- Managed = similar cost to Pinecone

### Option 3: Chroma (Open Source)
**Pros:**
- Developer-friendly
- Easy local development
- Good documentation
- Active community

**Cons:**
- Not production-ready for scale
- Less mature
- Limited managed option

### Option 4: Qdrant (Open Source + Managed)
**Pros:**
- Rust-based (fast)
- Good Python client
- Self-hosted or Qdrant Cloud
- Growing community

**Cons:**
- Smaller ecosystem than Pinecone
- Newer (less battle-tested)

### Option 5: Self-Hosted (PostgreSQL + pgvector)
**Pros:**
- Full control
- No external dependencies
- SQL interface
- Cheap (just server cost)

**Cons:**
- Setup complexity
- Scaling challenges
- Maintenance overhead

## Recommendation: Pinecone

**Why:**
1. **Fastest time to market** – no ops, just code
2. **Production-ready** – built for scale
3. **Cost acceptable** – $20/month is fine for MVP
4. **Focus on product** – not infrastructure
5. **Can migrate later** – data export possible

**Alternative:** Start with Chroma for dev, migrate to Pinecone for prod.

## Next Steps (Without Asking)

1. ✅ Research complete (this doc)
2. 🔄 Create Pinecone account (free tier)
3. 🔄 Install Python client
4. 🔄 Build ContextKeeper prototype
5. 🔄 Test save/retrieve context

## Technical Architecture

```
Agent Input → Compress Context → Vector Embedding → Pinecone Store
                                                      ↓
Agent Needs Context ← Retrieve Similar ← Query Vector ←┘
```

## Compression Strategy
- Use Claw Compactor patterns
- Summarize before embedding
- Store raw + compressed
- Evict old context (LRU)

## Base Integration
- Store context hash on Base
- Prove persistence
- Query fees in ROGER

---
*Research complete. Building starts NOW.*
