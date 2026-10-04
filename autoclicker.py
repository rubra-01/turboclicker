#!/usr/bin/env python3
import asyncio
import sys
from playwright.async_api import async_playwright

class SilentAutoClicker:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        self.running = True

    async def init(self, headless=False):
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(
            headless=headless,
            args=[
                '--disable-gpu',
                '--disable-dev-shm-usage',
                '--disable-software-rasterizer',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
                '--disable-extensions',
                '--disable-background-networking',
                '--disable-default-apps',
                '--disable-sync',
                '--disable-translate',
                '--hide-scrollbars',
                '--metrics-recording-only',
                '--mute-audio',
                '--no-first-run',
                '--safebrowsing-disable-auto-update'
            ]
        )
        self.context = await self.browser.new_context(
            viewport={'width': 1280, 'height': 4000},
            java_script_enabled=True,
            ignore_https_errors=True,
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        self.page = await self.context.new_page()
        
        # Block ads and tracking
        ad_domains = [
            '*.doubleclick.net',
            '*.googlesyndication.com',
            '*.googleadservices.com',
            '*.googletagmanager.com',
            '*.google-analytics.com',
            '*.facebook.com/tr*',
            '*.connect.facebook.net',
            '*.amazon-adsystem.com',
            '*.adnxs.com',
            '*.outbrain.com',
            '*.taboola.com',
            '*.criteo.com',
            '*.ads.twitter.com',
            '*.analytics.twitter.com'
        ]
        
        async def block_ads(route):
            for domain in ad_domains:
                if domain.replace('*', '') in route.request.url:
                    await route.abort()
                    return
            await route.continue_()
        
        await self.page.route('**', block_ads)
        
        # Set up page event to handle popups
        self.context.on('page', self.handle_new_page)

    async def handle_new_page(self, page):
        asyncio.create_task(page.close())

    async def navigate_to_site(self):
        await self.page.goto('https://greatonlinetools.com/autoliker/', timeout=60000)
        await self.page.wait_for_load_state('networkidle', timeout=30000)

    async def scroll_to_find_element(self, selector, max_scrolls=20):
        for _ in range(max_scrolls):
            try:
                element = self.page.locator(selector).first
                if await element.is_visible(timeout=10):
                    await element.scroll_into_view_if_needed()
                    return element
            except:
                pass
            await self.page.evaluate('window.scrollBy(0, 300)')
        return None

    async def enter_username(self):
        selectors = [
            'input[type="text"]',
            'input[name="username"]',
            'input[placeholder*="username"]',
            'input[placeholder*="Username"]',
            'input[type="text"][placeholder*="user"]',
            'input[name*="user"]'
        ]
        for selector in selectors:
            try:
                element = await self.scroll_to_find_element(selector, max_scrolls=30)
                if element:
                    await element.fill('rubrastudios')
                    await asyncio.sleep(0.5)
                    return
            except:
                continue

    async def click_search(self):
        try:
            await self.page.click('button:has-text("Search"), button:has-text("search"), input[type="submit"]', timeout=5000)
            await asyncio.sleep(2)
        except:
            try:
                await self.page.click('text=Search', timeout=3000)
                await asyncio.sleep(2)
            except:
                pass

    async def wait_for_dashboard(self):
        await asyncio.sleep(3)
        try:
            await self.page.wait_for_load_state('load', timeout=10000)
        except:
            pass
        await asyncio.sleep(2)

    async def click_earn_credits(self):
        selectors = [
            'text=Earn Credits',
            'a:has-text("Earn Credits")',
            'button:has-text("Earn Credits")',
            'a:has-text("Earn")',
            'button:has-text("Earn")',
            'text=Earn',
            '[href*="earn"]',
            '[class*="earn"]'
        ]
        for selector in selectors:
            try:
                element = await self.scroll_to_find_element(selector, max_scrolls=30)
                if element:
                    await element.click(timeout=5000)
                    await asyncio.sleep(2)
                    return
            except:
                continue

    async def check_if_on_search_page(self):
        """Check if we're back on the search page"""
        selectors = [
            'input[type="text"]',
            'input[name="username"]',
            'input[placeholder*="username"]',
            'input[placeholder*="Username"]'
        ]
        for selector in selectors:
            try:
                element = self.page.locator(selector).first
                if await element.is_visible(timeout=1):
                    return True
            except:
                continue
        return False

    async def auto_click_loop(self):
        while self.running:
            try:
                # Close any extra pages immediately (parallel)
                pages = self.context.pages
                if len(pages) > 1:
                    await asyncio.gather(*[p.close() for p in pages[1:]])
                
                # Check if we've been redirected to search page
                if await self.check_if_on_search_page():
                    await self.enter_username()
                    await self.click_search()
                    await self.wait_for_dashboard()
                    await self.click_earn_credits()
                    continue
                
                # Look for buttons (no scrolling needed - viewport is 4000px)
                selectors = [
                    'button:has-text("Like")',
                    'button:has-text("like")',
                    'button:has-text("Follow")',
                    'button:has-text("follow")',
                    'button:has-text("Verify")',
                    'button:has-text("verify")',
                    'a:has-text("Like")',
                    'a:has-text("like")',
                    'a:has-text("Follow")',
                    'a:has-text("follow")',
                    'a:has-text("Verify")',
                    'a:has-text("verify")',
                    'button:has-text("verify to")',
                    'button:has-text("Verify to")'
                ]
                
                for selector in selectors:
                    try:
                        element = self.page.locator(selector).first
                        if await element.is_visible(timeout=5):
                            await element.click(timeout=5)
                    except:
                        continue
                
            except Exception:
                pass

    async def run(self, headless=False):
        try:
            await self.init(headless)
            await self.navigate_to_site()
            await self.enter_username()
            await self.click_search()
            await self.wait_for_dashboard()
            await self.click_earn_credits()
            await self.auto_click_loop()
        except KeyboardInterrupt:
            self.running = False
        except Exception:
            pass
        finally:
            try:
                if self.browser:
                    await self.browser.close()
            except:
                pass

async def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    args = parser.parse_args()
    
    clicker = SilentAutoClicker()
    await clicker.run(headless=args.headless)

if __name__ == '__main__':
    asyncio.run(main())
