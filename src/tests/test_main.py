"""
Tests for main.py
"""

import pytest

import sys

from main import App


@pytest.fixture
def app_test():
    app_test = App(sys.argv)
    return app_test
