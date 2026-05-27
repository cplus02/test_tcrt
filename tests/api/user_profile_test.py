"""User profile API tests using the `*_test.py` naming convention — PYTEST."""
from __future__ import annotations

import pytest


@pytest.mark.api
@pytest.mark.tcrt("TCG-100558-010-010", link_type="primary")
def test_get_my_profile(base_url, api_token):
    assert base_url and api_token


@pytest.mark.api
@pytest.mark.tcrt("TCG-100558-020-010", link_type="covers")
def test_update_avatar(base_url, api_token):
    assert True


@pytest.mark.api
@pytest.mark.tcrt("TCG-100558-030-010", link_type="covers")
def test_change_display_name(base_url, api_token):
    assert True
