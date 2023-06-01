"""
Tests for directory_popup.py
"""

from src.views.directory_popup import DirectoryView


def test_directory_popup():
    test_view = DirectoryView(None, None)
    assert test_view.config == None
