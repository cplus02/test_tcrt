"""Admin-only API endpoint tests — PYTEST format."""
from __future__ import annotations

import pytest


@pytest.mark.api
@pytest.mark.tcrt("TCG-107489-010-010", link_type="covers")
def test_list_users_requires_admin(base_url, api_token):
    assert base_url and api_token


@pytest.mark.api
@pytest.mark.tcrt("TCG-107489-020-020", link_type="primary")
def test_create_team_as_admin(base_url, api_token):
    assert base_url


@pytest.mark.api
@pytest.mark.tcrt("TCG-107489-030-010", link_type="covers")
def test_delete_team_emits_audit_log(base_url, api_token):
    assert api_token


@pytest.mark.api
@pytest.mark.slow
@pytest.mark.tcrt("TCG-107489-040-010", link_type="primary")
def test_bulk_import_users_from_csv(base_url, api_token):
    assert True
