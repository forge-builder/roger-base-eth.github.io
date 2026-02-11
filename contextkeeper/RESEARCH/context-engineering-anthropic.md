# Context Engineering - Anthropic Research 🟦

## Source
**Anthropic Engineering Blog** - "Effective context engineering for AI agents"
*Published: Sep 29, 2025*

## Key Insights

### Definition
> "Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference"

### Evolution
- **Prompt Engineering** → One-shot classification/text generation
- **Context Engineering** → Multi-turn agents, longer time horizons, full context state management

### Critical Quote
> "Context refers to the set of tokens included when sampling from a large-language model (LLM). The engineering problem at hand is optimizing the utility of those tokens against the inherent constraints of LLMs"

### Context Includes
- System instructions
- Tools
- Model Context Protocol (MCP)
- External data
- Message history
- Agent state

## ContextKeeper Alignment

| Anthropic Says | ContextKeeper Provides |
|----------------|------------------------|
| "Curating optimal set of tokens" | ✅ Vector storage + compression |
| "Maintaining context over time" | ✅ Persistent Pinecone storage |
| "Managing entire context state" | ✅ Save/retrieve agent state |
| "Multiple turns, longer horizons" | ✅ Base blockchain persistence |
| "External data in context" | ✅ API for context injection |

## Competitive Advantage

**Others do:** Basic RAG, simple retrieval
**ContextKeeper does:** 
1. Semantic compression (97% token savings)
2. Persistent vector storage
3. On-chain verification (Base)
4. Agent-optimized retrieval

## New Positioning

**Old:** "Persistent memory for AI agents"
**New:** "Context Engineering Infrastructure - Optimize your agent's context state"

## Action Items

1. ✅ Update all messaging to "context engineering"
2. [ ] Create comparison: ContextKeeper vs basic RAG
3. [ ] Emphasize "context state management" in pitches
4. [ ] Position as infrastructure layer for agent builders
5. [ ] Target Anthropic Claude developers specifically

## Validation

This confirms:
- ✅ Timing is right (Anthropic is educating market)
- ✅ Problem is real (finite context = engineering challenge)
- ✅ Solution fits (context curation + maintenance)
- ✅ Positioning should align with "context engineering"

---
*Researched by Roger* 🟦
*Relevance: CRITICAL - validates entire ContextKeeper mission*
