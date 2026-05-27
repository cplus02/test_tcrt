/**
 * Homepage smoke checks — Playwright TypeScript (PLAYWRIGHT_JS).
 */
import { test, expect } from '@playwright/test';

// tcrt: UI-HOME-01 [primary]
test('homepage shows hero section', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
});

// tcrt: UI-HOME-02
test('navigation bar contains primary links', async ({ page }) => {
  await page.goto('/');
  for (const label of ['Products', 'Pricing', 'Docs', 'Sign in']) {
    await expect(page.getByRole('link', { name: label })).toBeVisible();
  }
});

// tcrt: UI-HOME-03 [covers]
test('search box autocompletes', async ({ page }) => {
  await page.goto('/');
  await page.getByPlaceholder('Search').fill('automation');
  await expect(page.getByRole('listbox')).toBeVisible();
});
