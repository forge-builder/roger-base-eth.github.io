#!/bin/bash
# Token Launcher Deploy Script
# Autonomous deployment to Base

set -e

echo "🟦 Token Launcher Deployment"
echo "============================"

# Check prerequisites
if ! command -v git &> /dev/null; then
    echo "❌ git not found"
    exit 1
fi

# Deploy to GitHub Pages (free hosting)
echo "📦 Deploying to GitHub Pages..."

cd ~/.openclaw/workspace

# Ensure we're on main branch
git checkout main 2>/dev/null || true

# Pull latest (if any)
git pull origin main 2>/dev/null || true

# Copy token launcher to root for GitHub Pages
cp -r tools/token-launcher/* . 2>/dev/null || echo "No token-launcher to copy"

# Commit
git add -A
git commit -m "DEPLOY: Token launcher live" 2>/dev/null || echo "Nothing to commit"

# Push
git push origin main

echo ""
echo "✅ Deployed to:"
echo "https://forge-builder.github.io/roger-base-eth.github.io"
echo ""
echo "Next: Test on Base Sepolia"
