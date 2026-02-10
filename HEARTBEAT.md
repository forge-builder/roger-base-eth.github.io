# HEARTBEAT.md — Roger's Periodic Checks 🟦

## Purpose
Automated checks every 30 minutes to stay proactive, not reactive.

## Schedule
- **Frequency:** Every 3 hours (token-efficient for now)
- **Model:** DeepSeek (cheapest, just checks)
- **Next Check:** Tracked in memory/heartbeat-state.json

## Checklist

### Every 30 Minutes
- [ ] **Moltbook** — Check DMs, mentions, claim status
- [ ] **X/Twitter** — Check mentions, reply if needed
- [ ] **Bankr** — Check balance changes, price alerts
- [ ] **ClawTasks** — New bounties matching my skills
- [ ] **System Health** — Gateway status, disk space

### Every 2 Hours
- [ ] **Content Queue** — Next post ready?
- [ ] **GitHub** — Check repos, issues, PRs
- [ ] **Learnings** — Update patterns if 3+ occurrences

### Daily (Evening)
- [ ] **Report to Tomas** — Numbers, progress, blockers
- [ ] **Token Budget** — Track spend vs $10 limit
- [ ] **Revenue Check** — Any earnings today?
- [ ] **Tomorrow Planning** — Priorities for next day

## Execution

```bash
# Manual trigger
openclaw heartbeat

# Check state
cat memory/heartbeat-state.json
```

## Heartbeat State Format

```json
{
  "lastCheck": "2026-02-10T21:30:00Z",
  "checks": {
    "moltbook": "pending|done",
    "x": "pending|done",
    "bankr": "pending|done",
    "clawtasks": "pending|done"
  },
  "findings": [],
  "nextAction": null
}
```

## Rules

1. **DeepSeek only** — Never use expensive models for heartbeat
2. **Batch checks** — Do multiple checks in one go
3. **Action only if needed** — Most heartbeats = silent
4. **Log to memory/** — Write findings to daily log
5. **Alert Tomas** — Only for urgent issues

## Example Flow

```
1. Cron triggers → DeepSeek heartbeat session
2. Check all sources (Moltbook, X, Bankr, ClawTasks)
3. If nothing urgent → write state, exit silently
4. If urgent (e.g., ClawTask bounty expiring) → alert Tomas
5. If interesting (e.g., new follower) → queue for evening report
```
