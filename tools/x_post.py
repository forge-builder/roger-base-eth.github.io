#!/usr/bin/env python3
"""
Roger's X Posting System — Mit Login-Unterstützung
"""

import asyncio
import random
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

USER_DATA_DIR = Path.home() / ".openclaw" / "browser" / "x-session"
SCREENSHOTS_DIR = Path.home() / ".openclaw" / "workspace" / "logs" / "screenshots"
LOG_FILE = Path.home() / ".openclaw" / "workspace" / "logs" / "posts.jsonl"

SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

async def check_logged_in(page):
    """Check if we're logged into X"""
    try:
        await page.goto("https://x.com/home", wait_until="domcontentloaded", timeout=10000)
        await asyncio.sleep(2)
        # Check for home timeline indicator
        return await page.query_selector("[data-testid='primaryColumn']") is not None
    except:
        return False

async def type_like_human(page, selector, text):
    """Type text with human-like speed"""
    await page.click(selector)
    await asyncio.sleep(random.uniform(0.1, 0.3))
    for char in text:
        await page.type(selector, char, delay=random.randint(50, 150))
        await asyncio.sleep(random.uniform(0.01, 0.05))

async def post_to_x(text: str, interactive=False) -> dict:
    """Post to X"""
    result = {
        "timestamp": datetime.now().isoformat(),
        "text": text,
        "status": "failed",
        "method": "playwright",
        "errors": [],
        "screenshot": None
    }
    
    async with async_playwright() as p:
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=str(USER_DATA_DIR),
            headless=False,
            args=['--disable-blink-features=AutomationControlled']
        )
        
        page = await browser.new_page()
        
        try:
            # Check if logged in
            print("🔐 Checking login status...")
            is_logged_in = await check_logged_in(page)
            
            if not is_logged_in:
                if interactive:
                    print("\n" + "="*60)
                    print("⚠️  NICHT EINGELOGGT")
                    print("="*60)
                    print("Bitte im Browser einloggen:")
                    print("1. X.com öffnen (ist bereits geöffnet)")
                    print("2. Mit forge.base.eth@gmail.com einloggen")
                    print("3. Dann hier ENTER drücken")
                    print("="*60)
                    input("\nEnter wenn eingeloggt...")
                    
                    # Re-check
                    is_logged_in = await check_logged_in(page)
                    if not is_logged_in:
                        raise Exception("Noch nicht eingeloggt")
                else:
                    raise Exception("Nicht eingeloggt. Starte mit --login flag")
            
            print("✅ Eingeloggt! Öffne Composer...")
            
            # Navigate to compose
            await page.goto("https://x.com/compose/post", wait_until="domcontentloaded")
            await asyncio.sleep(random.uniform(3, 5))
            
            # Find and fill text input
            print("📝 Schreibe Post...")
            text_input = await page.wait_for_selector(
                "div[role='textbox']", 
                timeout=10000
            )
            
            await type_like_human(page, "div[role='textbox']", text)
            await asyncio.sleep(random.uniform(1, 3))
            
            # Click post
            print("🚀 Klicke Post...")
            post_btn = await page.wait_for_selector(
                "button:has-text('Post')",
                timeout=10000
            )
            await post_btn.click()
            
            # Wait and verify
            await asyncio.sleep(random.uniform(4, 6))
            
            current_url = page.url
            if "/status/" in current_url:
                result["status"] = "success"
                result["url"] = current_url
                print(f"✅ ERFOLG! {current_url}")
            else:
                # Check for success toast
                toast = await page.query_selector("[data-testid='toast']")
                if toast:
                    result["status"] = "success"
                    print("✅ ERFOLG (Toast bestätigt)")
                else:
                    raise Exception("Konnte Erfolg nicht verifizieren")
                    
        except Exception as e:
            result["errors"].append(str(e))
            print(f"❌ FEHLER: {e}")
            
            # Screenshot
            try:
                screenshot_path = SCREENSHOTS_DIR / f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                await page.screenshot(path=str(screenshot_path))
                result["screenshot"] = str(screenshot_path)
                print(f"📸 Screenshot: {screenshot_path}")
            except:
                pass
        
        finally:
            await browser.close()
            
            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(result) + "\n")
        
        return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 x_post.py 'Tweet text' [--login]")
        sys.exit(1)
    
    tweet_text = sys.argv[1]
    interactive = "--login" in sys.argv
    
    print(f"🟦 Roger X-Posting: {tweet_text[:50]}...")
    result = asyncio.run(post_to_x(tweet_text, interactive))
    
    sys.exit(0 if result["status"] == "success" else 1)
