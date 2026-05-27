/**
 * UI login flow — Playwright TypeScript (PLAYWRIGHT_JS).
 *
 * // tcrt: comment must be on the line immediately before test(...) — no blank
 * line in between, or TCRT records an orphan_marker_comment warning.
 *
 * AUTH-001 / AUTH-002 / AUTH-003 intentionally overlap with test_user_auth.py
 * to show that one manual TC can be covered by scripts in multiple formats.
 */
import { test, expect } from '@playwright/test';

test.describe('Login page', () => {
  // tcrt: AUTH-001 [references]
  test('renders login form on first visit', async ({ page }) => {
    await page.goto('/login');
    await expect(page.getByRole('heading', { name: /sign in/i })).toBeVisible();
  });

  // tcrt: AUTH-002
  test('shows error toast on wrong credentials', async ({ page }) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('wrong');
    await page.getByRole('button', { name: /sign in/i }).click();
    await expect(page.getByText(/invalid credentials/i)).toBeVisible();
  });

  // tcrt: AUTH-001, AUTH-003 [covers]
  test('redirects to dashboard after successful login', async ({ page }) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill('demo@example.com');
    await page.getByLabel('Password').fill('demo-password');
    await page.getByRole('button', { name: /sign in/i }).click();
    await expect(page).toHaveURL(/\/dashboard$/);
  });
});
