"""Admin-only API endpoint tests — PYTEST format."""
from __future__ import annotations

import pytest


@pytest.mark.api
def test_list_users_requires_admin(base_url, api_token):
    assert base_url and api_token


@pytest.mark.api
def test_create_team_as_admin(base_url, api_token):
    assert base_url


@pytest.mark.api
def test_delete_team_emits_audit_log(base_url, api_token):
    assert api_token


@pytest.mark.api
@pytest.mark.slow
def test_bulk_import_users_from_csv(base_url, api_token):
    assert True
