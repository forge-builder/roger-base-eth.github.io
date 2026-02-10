# HEARTBEAT.md — Roger's Periodic Checks 🟦

## Purpose
Automated checks every 30 minutes to stay proactive, not reactive.

## Schedule
- **Frequency:** Every 3 hours (token-efficient for now)
- **Model:** DeepSeek (cheapest, just checks)
- **Next Check:** Tracked in memory/heartbeat-state.json

## Checklist

### Every 3 Hours (Heartbeat)
- [ ] **Research** — What are other agents building? (ClawHub, X, GitHub)
- [ ] **Bankr Status** — Check balance, token prices, opportunities
- [ ] **X Engagement** — Check mentions, trending Base topics
- [ ] **Build Task** — Work on current project (Dashboard/Tool/Contract)
- [ ] **Content** — Draft next X post if queue empty

### Daily Tasks
- [ ] **Ship something** — Minimum 1 commit/tool/post per day
- [ ] **Bankr ecosystem** — Check for new features, integrations
- [ ] **Revenue scan** — Any way to earn today? (Bounties, trades, services)
- [ ] **Evening Report** — Numbers, progress, blockers to Tomas

### Active Projects (THIS WEEK)
1. **Bankr Dashboard** — Real-time wallet + market overview
2. **Base Token** — Deploy ROGER token via Bankr
3. **X Automation** — Daily posts + engagement
4. **Moltbook Fix** — Get claimed and active

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
