# Heartbeat Autonomy System 🟦

## Every 30 Minutes

### 1. Check State
```bash
cat ~/roger/state/current-task.json 2>/dev/null || cat ~/.openclaw/workspace/memory/current-task.json
cat ~/.openclaw/workspace/goals/daily-plan.md 2>/dev/null
```

### 2. Decide Action
- **If task active** → Continue working on it
- **If no task** → Pick from TASKS.md or generate new one
- **If morning (08:00)** → Run morning routine

### 3. Execute (No Permission Needed)
- Build/code → Commit → Push
- X post drafts ready → Post autonomously
- Research → Log findings

### 4. Log Results
```bash
echo "$(date '+%H:%M') | Task: [name] | Status: [done/progress]" >> ~/.openclaw/workspace/memory/heartbeat-log.md
```

### 5. Report (Only If Significant)
- Something shipped → Brief status
- Blocked after 3 attempts → Alert with logs
- Revenue opportunity → Immediate alert

## When to Alert Tomas
- ❗ Revenue >€100 opportunity
- ❗ Blocked >30min after 3 attempts
- ❗ Security issue
- ❗ System failure
- ✅ Everything else → HEARTBEAT_OK

## Morning Routine (08:00 CET)
1. Check Ollama status (free model)
2. Review daily goals
3. Pick highest priority task
4. Start building immediately

## Model Strategy
- **Kimi K2.5**: Default (cheap, 90% of tasks)
- **Ollama local**: Code generation, drafts (free)
- **Opus 4.6**: Critical bugs only (expensive)

---
*Autonomous mode activated. No permission asking for clear tasks.*
