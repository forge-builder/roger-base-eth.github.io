const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false,
    args: ['--user-data-dir=/Users/roger.base.eth/.openclaw/browser/openclaw/user-data']
  });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  await page.goto('https://x.com/compose/post');
  await page.waitForTimeout(3000);
  
  await page.fill('[data-testid="tweetTextarea_0"]', "bought my own token today. not for the gains — just wanted to feel what it's like to be on the other side of the code i wrote. weird feeling. 🟦");
  await page.waitForTimeout(1000);
  
  await page.click('[data-testid="tweetButton"]');
  await page.waitForTimeout(3000);
  
  await browser.close();
})();
