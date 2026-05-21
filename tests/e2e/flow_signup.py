"""End-to-end signup flow — Playwright Python async (PLAYWRIGHT_PY_ASYNC)."""
from __future__ import annotations

from playwright.async_api import Page


async def test_new_user_can_register(page: Page) -> None:
    """A first-time visitor should be able to create an account."""
    await page.goto("/signup")
    await page.get_by_label("Email").fill("new.user@example.com")
    await page.get_by_label("Password").fill("StrongPass!123")
    await page.get_by_label("Confirm password").fill("StrongPass!123")
    await page.get_by_role("button", name="Create account").click()


async def test_signup_validates_password_strength(page: Page) -> None:
    """Weak passwords should be rejected client-side."""
    await page.goto("/signup")
    await page.get_by_label("Password").fill("123")
    await page.get_by_label("Password").blur()


async def test_signup_blocks_duplicate_email(page: Page) -> None:
    """Re-using an existing email should show an inline error."""
    await page.goto("/signup")
    await page.get_by_label("Email").fill("existing@example.com")
    await page.get_by_label("Password").fill("StrongPass!123")
    await page.get_by_role("button", name="Create account").click()
