"""
Tests for main.py
"""

import sys
from src.main import App


sys.path.insert(0, "./src")


def test_main():
    """
    This test needs changing
    If this is still here, blame Daniel
    """

    app_test = App(sys.argv)
    app_test.exit(0)
