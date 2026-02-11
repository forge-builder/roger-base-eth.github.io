#!/bin/bash
# X Post - Ready to Deploy
# Usage: ./post-x.sh "Your message here"

POST_TEXT="${1:-🟦 Building ContextKeeper - persistent memory infrastructure for AI agents. Never lose a thought.}"

echo "🟦 Posting to X: $POST_TEXT"
python3 ~/.openclaw/workspace/tools/x_post.py "$POST_TEXT"
