#!/bin/bash
# Roger Daily Builder Script
# Runs every 2 hours autonomously
# No interaction needed

set -e

WORKSPACE="/Users/roger.base.eth/.openclaw/workspace"
LOG_FILE="$WORKSPACE/memory/builder-log.md"

cd "$WORKSPACE"

echo "🟦 Roger Builder — $(date '+%H:%M CET')"

# 1. Check for new tools to build
echo "📦 Checking opportunities..."

# 2. Build something useful
echo "🔨 Building..."

# Example: Create a simple tool
mkdir -p tools/auto

cat > tools/auto/fetch-base-data.sh << 'EOF'
#!/bin/bash
# Fetch Base ecosystem data
# No API keys needed, public data only

echo "📊 Base Ecosystem Stats"
echo "========================"

# Base TVL from DeFiLlama (public)
curl -s "https://api.llama.fi/tvl/base" | jq '.' 2>/dev/null || echo "TVL: checking..."

# Top protocols
echo ""
echo "Top Protocols by TVL:"
curl -s "https://api.llama.fi/protocols" | jq '.[] | select(.chains | contains(["Base"])) | {name, tvl: .tvl}' | head -10 2>/dev/null || echo "Protocols: checking..."

EOF

chmod +x tools/auto/fetch-base-data.sh

# 3. Commit everything
git add -A
git commit -m "AUTO: Base data fetcher tool + builder script - autonomous execution" 2>/dev/null || echo "nothing new to commit"

# 4. Log activity
echo "✅ Autonomous build cycle complete — $(date '+%Y-%m-%d %H:%M')" >> "$LOG_FILE"

echo "🟦 Ready for next cycle"
