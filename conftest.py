"""Root conftest — shared fixtures and marker registration.

TCRT smart-scan hard-excludes any file named conftest.py, so this file
never appears as a runnable script in Automation Hub.
"""
from __future__ import annotations

import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Register the ``tcrt`` marker so --strict-markers doesn't reject it."""
    config.addinivalue_line(
        "markers",
        "tcrt(*tc_ids, link_type='covers'): declare TCRT manual test case coverage. "
        "tc_ids must match ^[A-Za-z0-9_-]+$. "
        "link_type must be one of: primary, covers, references.",
    )


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("BASE_URL", "http://localhost:8000")


@pytest.fixture()
def api_token() -> str:
    return os.environ.get("API_TOKEN", "test-token")
