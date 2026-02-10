#!/bin/bash
# Roger Status Checker - Quick system overview for Roger 🟦

echo "=== Roger Status ==="
echo "Date: $(date)"
echo ""

echo "=== X/Twitter ==="
bird whoami 2>/dev/null | grep -E "🙋|Status" || echo "X: Rate limited or not connected"
echo ""

echo "=== Bankr Wallet ==="
echo "EVM: 0x984d6741e2c6559b1e655b6dbb3a38662fe2c123"
echo "Solana: AeyePdw7yk3QdfJP3EzNpyy4EF5hgtxkcxPCMKHAYp2y"
echo ""

echo "=== OpenClaw ==="
openclaw status 2>&1 | grep -E "Runtime|Model|Gateway" | head -5
echo ""

echo "=== Workspace ==="
cd /Users/roger.base.eth/.openclaw/workspace && git log --oneline -3 2>/dev/null || echo "Git: No commits"
echo ""

echo "=== Done ==="
