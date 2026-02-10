# Roger's Sub-Agent System 🟦

## Mission Control Setup

### Agent Roster

| Agent | Role | Model | Cost | Tasks |
|-------|------|-------|------|-------|
| **Roger-Core** | Coordinator | Kimi K2.5 | ~$0.001/1k | Decision making, user interface |
| **Scout** | Researcher | DeepSeek v3.2 | ~$0.0002/1k | Web research, trend monitoring |
| **Coder** | Developer | Haiku 4.5 | ~$0.003/1k | Code generation, debugging |
| **Trader** | Finance | Kimi K2.5 | ~$0.001/1k | Bankr operations, market analysis |
| **Writer** | Content | DeepSeek v3.2 | ~$0.0002/1k | X posts, Moltbook, essays |

### Model Strategy (Budget-Optimized)

**Free/Cheap Options:**
- DeepSeek v3.2: $0.00000025/token (cheapest)
- Haiku 4.5: $0.003/1k (good for code)
- Kimi K2.5: $0.001/1k (default for everything)

**Spawn Command:**
```bash
# Spawn Scout for research
sessions_spawn agent=scout model=deepseek/deepseek-chat task="Research X trends"

# Spawn Coder for building
sessions_spawn agent=coder model=anthropic/claude-sonnet-4-5 task="Build feature X"
```

### Communication Protocol

1. **Roger-Core** receives task
2. Decides which sub-agent to spawn
3. Spawns agent with specific task + model
4. Sub-agent works independently
5. Returns results to Roger-Core
6. Roger-Core integrates and ships

### Cost Control

- Scout/Writer: DeepSeek (90% savings)
- Coder: Haiku (good code, cheap)
- Complex tasks: Kimi (default)
- Emergency: Opus (rare)

### Tonight's Tasks (Autonomous)

1. **Scout:** Monitor X for Base ecosystem news
2. **Writer:** Draft 3 X posts for tomorrow
3. **Coder:** Fix x_post.py timeout issues
4. **Trader:** Research Bankr token deployment
5. **Roger-Core:** Document learnings, update MEMORY.md

### Wake Conditions

Alert Tomas if:
- Bankr balance changes (ETH received)
- X mention requires reply
- Moltbook DM received
- Critical error in sub-agent
- Revenue opportunity found

---
*This runs autonomously while Tomas sleeps.*
