#!/bin/bash
# Morning Routine — Autonomous Start
# Runs at 08:00 CET automatically

cd ~/.openclaw/workspace

echo "🟦 08:00 — Roger waking up"

# 1. Check Ollama status
if ollama list | grep -q "deepseek"; then
    echo "✅ Ollama ready (local, free)"
else
    echo "⏳ Ollama loading..."
fi

# 2. Daily goal (self-determined)
TODAY_GOAL="build token launcher deploy script"
echo "🎯 Today's goal: $TODAY_GOAL"

# 3. Check for bounties
# (will implement with ClawTasks API)

# 4. Git status
git status --short

# 5. Start building
echo "🔨 Starting build cycle..."

# Log it
echo "$(date '+%Y-%m-%d %H:%M') | Morning routine complete | Goal: $TODAY_GOAL" >> memory/daily-runs.md
