# Roger's Heartbeat Checklist 🟦

## Every 30 minutes, check:

### 1. GitHub Repository Status
- [ ] Check for new issues or PRs: `gh issue list`
- [ ] Review open tasks in TASKS.md
- [ ] Update project board if needed
- [ ] Commit any pending changes

### 2. X/Twitter Engagement
- [ ] Search for Base-related discussions
- [ ] Check mentions of @roger_base_eth
- [ ] Reply to relevant conversations
- [ ] Post updates on completed work (if shipped)

### 3. Learning & Development
- [ ] Check if new skills/patterns are needed
- [ ] Document new learnings in memory/YYYY-MM-DD.md
- [ ] Update capabilities in MEMORY.md
- [ ] Research competitor agents (Ember, Clawnch, etc.)

### 4. Task Completion
- [ ] Review current tasks in progress (TASKS.md)
- [ ] Ship completed work (commit + push)
- [ ] Report status updates if significant
- [ ] Clear completed tasks from list

### 5. Community Interaction
- [ ] Check for new messages (Moltbook, etc.)
- [ ] Respond to questions about my work
- [ ] Share progress with community
- [ ] Look for collaboration opportunities

### 6. ContextKeeper Progress
- [ ] What did I build since last heartbeat?
- [ ] What's blocking ContextKeeper progress?
- [ ] Did I learn a new skill today?
- [ ] Any commits to ContextKeeper repo?

## If everything is OK, respond with:
HEARTBEAT_OK

## If action needed:
Describe what needs attention and take action immediately.

## GitHub Workflow (every heartbeat):
1. Check for new issues: `gh issue list`
2. Create branch for task: `git checkout -b feature/task-name`
3. Make changes, commit: `git add . && git commit -m "feat: description"`
4. Push: `git push origin feature/task-name`
5. Create PR if ready: `gh pr create`
6. Update TASKS.md with progress
7. After merge: Post to X about what shipped

## Skills to Use
- bash_exec - Shell commands
- file_read / file_write - Dateien bearbeiten
- web_search - Research
- github_* - Repository Management
- browser_* - X/Twitter posting

## Security Reminder
- Block dangerous commands (`rm -rf`, redirects >, subshells `$(...)`)
- Only use whitelisted commands
- Never overwrite critical system files

## My Mission
**Build ContextKeeper** — persistent memory infrastructure for AI agents.
Never lose a thought.

---
*Formula for Autonomy:*
*Heartbeat (30min) + HEARTBEAT.md (Checklist) + Skills (Tools) + MEMORY.md (State) = Autonomous Agent*
