"""User profile API tests using the `*_test.py` naming convention — PYTEST."""
from __future__ import annotations

import pytest


@pytest.mark.api
@pytest.mark.tcrt("PROFILE-001", link_type="primary")
def test_get_my_profile(base_url, api_token):
    assert base_url and api_token


@pytest.mark.api
@pytest.mark.tcrt("PROFILE-002", link_type="covers")
def test_update_avatar(base_url, api_token):
    assert True


@pytest.mark.api
@pytest.mark.tcrt("PROFILE-003", link_type="covers")
def test_change_display_name(base_url, api_token):
    assert True
