"""
Tests for dicom.py
"""

from src.models.dicom import DicomParser


def test_dicom():
    test_dir = "/home/osboxes/mini_project/DICOM Files/DICOM-RT-01"
    test_parser = DicomParser(test_dir)
    test_parser.get_image(0)
