/**
 * Checkout flow — Playwright JavaScript (.test.js → PLAYWRIGHT_JS).
 *
 * TCG-107489-130-010 intentionally overlaps with flow_purchase.py to show that the
 * same manual TC can be covered by both a JS spec and a Python e2e flow.
 */
const { test, expect } = require('@playwright/test');

test.describe('Checkout', () => {
  // tcrt: TCG-107489-130-010 [covers]
  test('adds an item to the cart', async ({ page }) => {
    await page.goto('/shop/widget');
    await page.getByRole('button', { name: /add to cart/i }).click();
    await expect(page.getByText(/1 item in cart/i)).toBeVisible();
  });

  // tcrt: TCG-107489-150-010
  test('updates total when quantity changes', async ({ page }) => {
    await page.goto('/cart');
    await page.getByLabel('Quantity').fill('3');
    await expect(page.getByTestId('cart-total')).toContainText('$');
  });

  // tcrt: TCG-107489-130-010, TCG-107489-140-010 [covers]
  test('completes purchase with valid payment', async ({ page }) => {
    await page.goto('/cart');
    await page.getByRole('button', { name: /checkout/i }).click();
    await page.getByLabel('Card number').fill('4242424242424242');
    await page.getByLabel('Expiry').fill('12/30');
    await page.getByLabel('CVC').fill('123');
    await page.getByRole('button', { name: /place order/i }).click();
    await expect(page).toHaveURL(/\/order\/[a-z0-9-]+$/);
  });
});
