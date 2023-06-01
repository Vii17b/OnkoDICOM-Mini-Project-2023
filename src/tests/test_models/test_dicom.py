"""
Tests for dicom.py
"""

import pytest
from src.models.dicom import DicomParser


@pytest.mark.parametrize('file_dir, exists',
    [
        ('/home/osboxes/mini_project/DICOM Files/DICOM-RT-01', True),
        ('/home', False)
    ]
)
def test_dicom(file_dir, exists):
    test_parser = DicomParser(file_dir)
    assert test_parser.read_directory(file_dir) == exists
    
    # For the file that exists, test that get_image returns something
    if not exists:
        return
    assert test_parser.get_image(0) != None
