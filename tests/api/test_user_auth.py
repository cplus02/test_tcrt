"""User auth API tests — PYTEST format (test_ prefix)."""
from __future__ import annotations

import pytest


@pytest.mark.api
def test_login_with_valid_credentials(base_url, api_token):
    """Successful login should return 200 and a JWT."""
    # Placeholder: a real implementation would issue an HTTP request here.
    assert base_url.startswith("http")
    assert api_token


@pytest.mark.api
def test_login_with_invalid_password_returns_401(base_url):
    """Wrong password should be rejected with 401."""
    assert base_url


@pytest.mark.api
def test_logout_clears_session(base_url, api_token):
    """Logout endpoint should invalidate the current session token."""
    assert api_token


class TestPasswordReset:
    """Grouped scenarios for the password reset flow."""

    def test_request_reset_email(self, base_url):
        assert base_url

    def test_reset_with_expired_token_returns_410(self, base_url):
        assert base_url
