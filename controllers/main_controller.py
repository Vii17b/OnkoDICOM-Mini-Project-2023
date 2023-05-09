"""
controller/main_controller.py
    - Imports
        - PySide6 -> QObject
        - os
        - models.dicom -> DicomObj
        - models.config -> Config
        - views.image_popup -> ImageView
        - views.directory_popup -> DirectoryView

    - Class: MainController(QObject)
        - The controller handles processes and contains logic
        - Effectively the main program
"""

import os
from PySide6.QtWidgets import QObject

from models.dicom import DicomParser
from models.config import Config
from views.image_popup import ImageView
from views.directory_popup import DirectoryView


class MainController(QObject):
    """
    Docstring
    """
    def __init__(self, model, parent=None) -> None:
        super().__init__(parent)

        # models
        self._main_model = model
        self._config = Config()
        self._dicom_parser = None

        # views
        self._image_popup = None

    @property
    def main_model(self):
        """
        Getter for _main_model
        """
        return self._main_model
