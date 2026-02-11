#!/usr/bin/env python3
"""
X Posting Script - Roger
Uses Playwright for browser automation (learned yesterday)
"""

import subprocess
import time
import sys

def post_to_x(text):
    """
    Post to X using browser automation
    Requires: X login session active in browser
    """
    
    script = f'''
const {{ chromium }} = require('playwright');

(async () => {{
    const browser = await chromium.launch({{ headless: false }});
    const context = await browser.newContext({{
        viewport: {{ width: 1280, height: 720 }}
    }});
    const page = await context.newPage();
    
    try {{
        // Navigate to compose
        await page.goto('https://x.com/compose/post');
        await page.waitForTimeout(3000);
        
        // Check if login required
        const loginButton = await page.$('text=Sign in');
        if (loginButton) {{
            console.log('LOGIN_REQUIRED');
            await browser.close();
            process.exit(1);
        }}
        
        // Type post text
        const textbox = await page.getByRole('textbox');
        await textbox.fill(`{text}`);
        await page.waitForTimeout(1000);
        
        // Click Post
        const postButton = await page.getByRole('button', {{ name: /post/i }});
        await postButton.click();
        await page.waitForTimeout(3000);
        
        console.log('SUCCESS');
        
    }} catch (error) {{
        console.log('ERROR:', error.message);
    }}
    
    await browser.close();
}})();
'''
    
    # Write and execute
    with open('/tmp/x_post.js', 'w') as f:
        f.write(script)
    
    result = subprocess.run(
        ['node', '/tmp/x_post.js'],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    return result.stdout.strip(), result.stderr.strip()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python x_post.py 'Your post text'")
        sys.exit(1)
    
    text = sys.argv[1]
    stdout, stderr = post_to_x(text)
    
    if 'LOGIN_REQUIRED' in stdout:
        print("❌ X login required - session expired")
        print("Fix: Login to x.com in browser first")
    elif 'SUCCESS' in stdout:
        print("✅ Posted to X successfully")
    else:
        print(f"⚠️ Result: {stdout}")
        if stderr:
            print(f"Error: {stderr}")
