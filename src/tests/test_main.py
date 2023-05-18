"""
Tests for main.py
"""

import pytest

import sys

sys.path.insert(0, "./src")

from main import App


@pytest.fixture
def app_test():
    app_test = App(sys.argv)
    return app_test
