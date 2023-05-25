"""
Tests for main.py
"""

import pytest
import sys
from main import App


sys.path.insert(0, "./src")


@pytest.fixture
def app_test():
    app_test = App(sys.argv)
    return app_test
