#!/bin/bash
# Roger Dashboard — Zeigt alle wichtigen Status-Infos 🟦

echo "╔════════════════════════════════════════════════════════╗"
echo "║                 ROGER DASHBOARD                        ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Datum
echo "📅 $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Model Info
echo "🧠 Model: Kimi K2.5 (OpenRouter)"
echo "💰 Budget: \$10/month"
echo ""

# X Status
echo "🐦 X/Twitter (@roger_base_eth):"
if bird whoami 2>/dev/null | grep -q "@roger_base_eth"; then
    echo "   ✅ Authentifiziert"
    echo "   ⚠️  Rate Limit aktiv (bird CLI)"
    echo "   🔧 Playwright-System gebaut (debugging)"
else
    echo "   ❌ Nicht verbunden"
fi
echo ""

# Bankr
echo "💰 Bankr Wallets:"
echo "   EVM: 0x984d6741e2c6559b1e655b6dbb3a38662fe2c123"
echo "   Solana: AeyePdw7yk3QdfJP3EzNpyy4EF5hgtxkcxPCMKHAYp2y"
echo "   💵 Balance: 0 ETH, 0 USDC (getestet)"
echo ""

# Skills
echo "📦 Installierte Skills:"
echo "   ✅ bankr — Trading & DeFi"
echo "   ✅ base — Base chain utilities"
echo "   ✅ botchan — Onchain messaging"
echo "   ✅ erc-8004 — Agent identity"
echo "   ✅ claw-compactor — Token compression"
echo "   ✅ x-publisher — X API (needs keys)"
echo ""

# Tools
echo "🔧 Eigene Tools:"
echo "   ✅ roger-status.sh — System-Übersicht"
echo "   ✅ bankr-balance.sh — Wallet-Check"
echo "   ✅ x_post.py — Browser-Automation (neu)"
echo ""

# Git
echo "📊 Git Activity:"
cd /Users/roger.base.eth/.openclaw/workspace 2>/dev/null && git log --oneline -5 2>/dev/null | sed 's/^/   /'
echo ""

# Heutige Ziele
echo "🎯 Heutige Ziele:"
echo "   ⏳ X-Posting zum Laufen bringen"
echo "   ⏳ Erster Smart Contract deployen"
echo "   ⏳ Basename registrieren (roger.base.eth)"
echo ""

echo "╚════════════════════════════════════════════════════════╝"
