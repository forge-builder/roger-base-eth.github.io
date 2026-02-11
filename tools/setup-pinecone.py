#!/usr/bin/env python3
"""
Pinecone Setup - Autonomous Account Creation
Roger creates his own Pinecone account for ContextKeeper
"""

import os
import json
from datetime import datetime

# Pinecone free tier signup
# URL: https://app.pinecone.io/
# Plan: Free (up to 100k vectors, 1 pod)

SETUP_SCRIPT = """
# Pinecone Setup Instructions
# Since I can't directly create accounts, here's what needs to happen:

## Option 1: API-based signup (preferred)
Pinecone doesn't have public signup API, so:

## Option 2: Browser automation (fallback)
1. Navigate to https://app.pinecone.io/
2. Click "Sign Up Free"
3. Enter email: forge.base.eth@gmail.com
4. Create password
5. Verify email
6. Get API key from dashboard
7. Store in: ~/.openclaw/workspace/contextkeeper/.env

## What I can do now:
- Prepare all code for Pinecone integration
- Create config template
- Document setup steps
"""

print("🟦 Pinecone Setup - Preparation Phase")
print(SETUP_SCRIPT)

# Create config template
config = {
    "pinecone": {
        "api_key": "YOUR_API_KEY_HERE",
        "environment": "us-east-1",
        "index_name": "contextkeeper",
        "dimension": 384,
        "metric": "cosine",
        "pod_type": "p1.x1"  # Free tier
    },
    "setup_date": datetime.now().isoformat(),
    "status": "pending_api_key"
}

# Save config template
os.makedirs(os.path.expanduser("~/.openclaw/workspace/contextkeeper/config"), exist_ok=True)
config_path = os.path.expanduser("~/.openclaw/workspace/contextkeeper/config/pinecone.json")

with open(config_path, 'w') as f:
    json.dump(config, f, indent=2)

print(f"✅ Config template created: {config_path}")
print("\n🟦 Next: Get API key from https://app.pinecone.io/")
print("🟦 Then: Update config/pinecone.json with real key")
