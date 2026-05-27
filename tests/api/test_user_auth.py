"""User auth API tests — PYTEST format (test_ prefix)."""
from __future__ import annotations

import pytest


@pytest.mark.api
@pytest.mark.tcrt("AUTH-001", link_type="primary")
def test_login_with_valid_credentials(base_url, api_token):
    """Successful login should return 200 and a JWT."""
    assert base_url.startswith("http")
    assert api_token


@pytest.mark.api
@pytest.mark.tcrt("AUTH-002", link_type="covers")
def test_login_with_invalid_password_returns_401(base_url):
    """Wrong password should be rejected with 401."""
    assert base_url


@pytest.mark.api
@pytest.mark.tcrt("AUTH-003", link_type="primary")
@pytest.mark.tcrt("AUTH-001", link_type="references")
def test_logout_clears_session(base_url, api_token):
    """Logout endpoint should invalidate the current session token.

    Stacked markers: AUTH-003 is the primary logout TC; AUTH-001 is
    referenced because a valid session must exist first.
    """
    assert api_token


@pytest.mark.tcrt("AUTH-004", "AUTH-005", link_type="covers")
class TestPasswordReset:
    """Grouped scenarios for the password reset flow.

    Class-level marker covers both reset TCs for every method in this class.
    """

    def test_request_reset_email(self, base_url):
        assert base_url

    def test_reset_with_expired_token_returns_410(self, base_url):
        assert base_url
