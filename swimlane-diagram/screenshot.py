"""
Converts an HTML swimlane diagram to PNG using Playwright.
Usage: python3 screenshot.py <input.html> <output.png>
"""
import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def screenshot(html_path: str, output_path: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_context(device_scale_factor=2)
        page = await page.new_page()
        await page.set_viewport_size({"width": 1600, "height": 900})
        await page.goto(f"file://{os.path.abspath(html_path)}")
        await page.wait_for_timeout(600)
        dims = await page.evaluate(
            "() => ({width: document.body.scrollWidth, height: document.body.scrollHeight})"
        )
        await page.set_viewport_size({
            "width": dims["width"] + 80,
            "height": dims["height"] + 80,
        })
        await page.screenshot(path=output_path, full_page=True)
        await browser.close()
    print(f"PNG saved: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 screenshot.py <input.html> <output.png>")
        sys.exit(1)
    asyncio.run(screenshot(sys.argv[1], sys.argv[2]))
