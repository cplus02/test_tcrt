"""End-to-end purchase flow — Playwright Python async (PLAYWRIGHT_PY_ASYNC).

Filename does NOT start with `test_` and does NOT end with `_test.py`,
so the storage provider classifies it as PLAYWRIGHT_PY_ASYNC rather than
PYTEST. Functions still use `test_` prefix so smart-scan can extract
test names from the AST.
"""
from __future__ import annotations

from playwright.async_api import Page, async_playwright


async def test_full_purchase_flow(page: Page) -> None:
    """Walk a guest user from search → cart → checkout → confirmation."""
    await page.goto("/")
    await page.get_by_role("link", name="Shop").click()
    await page.get_by_placeholder("Search").fill("notebook")
    await page.keyboard.press("Enter")
    await page.locator(".product-card").first.click()
    await page.get_by_role("button", name="Add to cart").click()
    await page.get_by_role("link", name="Cart").click()
    await page.get_by_role("button", name="Checkout").click()


async def test_apply_discount_code(page: Page) -> None:
    """A valid discount code should reduce the cart total."""
    await page.goto("/cart")
    await page.get_by_placeholder("Discount code").fill("WELCOME10")
    await page.get_by_role("button", name="Apply").click()


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await test_full_purchase_flow(page)
        await test_apply_discount_code(page)
        await browser.close()
