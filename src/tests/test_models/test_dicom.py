"""
Tests for dicom.py
"""

from models import dicom


def test_dicom():
    dicomParser_test = dicom.DicomParser("DICOM Files")
