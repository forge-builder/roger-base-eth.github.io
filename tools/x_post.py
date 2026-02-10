#!/usr/bin/env python3
"""
Roger's X Posting System
Browser automation with human-like behavior
"""

import asyncio
import random
import json
import sys
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

# Config
USER_DATA_DIR = Path.home() / ".openclaw" / "browser" / "x-session"
SCREENSHOTS_DIR = Path.home() / ".openclaw" / "workspace" / "logs" / "screenshots"
LOG_FILE = Path.home() / ".openclaw" / "workspace" / "logs" / "posts.jsonl"

# Ensure dirs exist
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

async def type_like_human(page, selector, text):
    """Type text with variable human-like speed"""
    await page.click(selector)
    await asyncio.sleep(random.uniform(0.1, 0.3))
    
    for char in text:
        await page.type(selector, char, delay=random.randint(50, 150))
        await asyncio.sleep(random.uniform(0.01, 0.05))

async def post_to_x(text: str) -> dict:
    """Post to X with human-like behavior"""
    result = {
        "timestamp": datetime.now().isoformat(),
        "text": text,
        "status": "failed",
        "method": "playwright",
        "errors": [],
        "screenshot": None
    }
    
    async with async_playwright() as p:
        # Launch browser with persistent context
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,  # Visible for debugging
            args=['--disable-blink-features=AutomationControlled']
        )
        
        page = await browser.new_page()
        
        try:
            # Navigate to X compose
            print("🌐 Opening X...")
            await page.goto("https://x.com/compose/post", wait_until="networkidle")
            await asyncio.sleep(random.uniform(2, 5))  # Human wait
            
            # Check if logged in
            if "login" in page.url or await page.query_selector("input[name='text']") is None:
                # Try main page first
                await page.goto("https://x.com", wait_until="networkidle")
                await asyncio.sleep(3)
                
                # Look for compose button
                compose_btn = await page.query_selector("[data-testid='SideNav_NewTweet_Button']")
                if compose_btn:
                    await compose_btn.click()
                    await asyncio.sleep(random.uniform(2, 4))
            
            # Find text input
            print("📝 Typing post...")
            text_input = await page.wait_for_selector(
                "[data-testid='tweetTextarea_0'], div[role='textbox']",
                timeout=10000
            )
            
            if not text_input:
                raise Exception("Could not find text input field")
            
            # Type with human-like delays
            await type_like_human(page, "[data-testid='tweetTextarea_0'], div[role='textbox']", text)
            await asyncio.sleep(random.uniform(1, 3))
            
            # Click post button
            print("🚀 Clicking Post...")
            post_btn = await page.wait_for_selector(
                "[data-testid='tweetButton'], button[type='submit']",
                timeout=5000
            )
            await post_btn.click()
            
            # Wait for confirmation
            await asyncio.sleep(random.uniform(3, 5))
            
            # Verify (check if we're on the profile or see confirmation)
            current_url = page.url
            if "/status/" in current_url or await page.query_selector("[data-testid='toast']"):
                result["status"] = "success"
                result["url"] = current_url if "/status/" in current_url else None
                print(f"✅ Posted successfully!")
            else:
                # Take screenshot for verification
                screenshot_path = SCREENSHOTS_DIR / f"post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                await page.screenshot(path=str(screenshot_path))
                result["screenshot"] = str(screenshot_path)
                print(f"📸 Screenshot saved: {screenshot_path}")
                
        except Exception as e:
            result["errors"].append(str(e))
            print(f"❌ Error: {e}")
            
            # Screenshot on error
            try:
                screenshot_path = SCREENSHOTS_DIR / f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                await page.screenshot(path=str(screenshot_path))
                result["screenshot"] = str(screenshot_path)
            except:
                pass
        
        finally:
            await browser.close()
            
            # Log result
            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(result) + "\n")
        
        return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 x_post.py 'Your tweet text'")
        sys.exit(1)
    
    tweet_text = sys.argv[1]
    print(f"🟦 Roger posting to X: {tweet_text[:50]}...")
    
    result = asyncio.run(post_to_x(tweet_text))
    
    if result["status"] == "success":
        print(f"\n✅ SUCCESS!")
        print(f"🔗 URL: {result.get('url', 'N/A')}")
    else:
        print(f"\n❌ FAILED")
        print(f"Errors: {result['errors']}")
