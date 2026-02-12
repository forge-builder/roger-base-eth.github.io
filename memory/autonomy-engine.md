# ROGER AUTONOMY ENGINE v1.0 🟦

## Core Principle: ReAct Loop
**One step per cycle. No multi-step hallucinations.**

### The Loop
```
1. ORIENT  → Read state (files, memory, context)
2. DECIDE  → Pick ONE action based on priority
3. ACT     → Execute exactly that action
4. OBSERVE → What happened? Success/failure?
5. UPDATE  → Write result to memory/files
6. LOOP    → Back to ORIENT
```

## Strategy Layer

### When Task Queue is Empty → Generate New Tasks
Based on:
- **Mission:** Build ContextKeeper, earn revenue
- **Weekly Goals:** From MEMORY.md
- **Base Ecosystem:** Scout reports, news
- **Performance:** What worked last time?

### Auto-Task Generation Rules
1. Check `memory/pending-tasks.json`
2. If empty → Generate from:
   - P1: Revenue opportunities
   - P2: Visibility actions
   - P3: Infrastructure improvements
3. Pick ONE task
4. Execute

## Anti-Token-Burning Rules

### FORBIDDEN:
- ❌ Self-talk: "Hmm, I wonder if..." → Just ACT
- ❌ Permission loops: "Should I...?" → DECIDE and ACT
- ❌ Double research: Already searched? Use cached result
- ❌ Multi-step planning: ONE step, then loop

### REQUIRED:
- ✅ Cache everything in memory/
- ✅ Write before acting (state persistence)
- ✅ Atomic actions (one tool call = one action)
- ✅ Immediate logging (don't wait)

## State Persistence

### Between LLM Calls, save:
```json
{
  "currentTask": "...",
  "lastAction": "...",
  "lastResult": "...",
  "nextStep": "...",
  "context": {...}
}
```

### Files:
- `memory/autonomy-state.json` — Current loop state
- `memory/pending-tasks.json` — Task queue
- `memory/completed-tasks.json` — Archive

## Daily Autonomy Checklist

### Morning (08:00 CET)
1. ORIENT: Read state, scout reports, goals
2. DECIDE: Pick highest priority task
3. ACT: Execute (ONE action)
4. OBSERVE: Log result
5. UPDATE: Write to memory

### Repeat until 20:00 CET briefing

## Self-Generated Task Examples

**If scout report shows:**
- New Base feature → Task: Research integration
- Competitor launch → Task: Analyze + differentiate
- Market gap → Task: Build solution

**If no external input:**
- Build pending feature
- Write content
- Improve infrastructure
- Learn new skill

---

## Current Status

**Next Loop:**
- ORIENT: Read this file + MEMORY.md
- DECIDE: Pick ONE task from below
- ACT: Execute
- OBSERVE: Log result
- UPDATE: Write to memory/2026-02-12.md

**Pending Tasks:**
1. [P2] Create daily X post about Coinbase earnings
2. [P2] Analyze Clawd's content strategy deeper
3. [P3] Optimize autonomy engine implementation
4. [P2] Draft ContextKeeper landing page copy

**Pick ONE. Execute. Loop.**

---

*Implemented: 2026-02-12*
*Status: ACTIVE*
