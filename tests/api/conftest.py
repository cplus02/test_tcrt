"""Shared API test fixtures.

This file is deliberately excluded by TCRT smart-scan (filename in
{__init__.py, conftest.py}) so it never appears as a runnable script in
Automation Hub.
"""
from __future__ import annotations

import os

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("BASE_URL", "http://localhost:8000")


@pytest.fixture()
def api_token() -> str:
    return os.environ.get("API_TOKEN", "test-token")
