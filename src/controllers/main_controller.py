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
from PySide6.QtCore import QObject

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
        self._config = Config(self)

        # views
        self._image_popup = None

    def config_resolved(self, config):
        """
        If the default directory database file already exists,
        this will be called directly after __init__()

        If the default dir does NOT exist,
        this will be called after the user enters it
        """
        self._dicom_parser = DicomParser(config.default_dir)
        self._main_model.dicom_directory = config.default_dir
        self._main_model.index = 0

    @property
    def main_model(self):
        """
        Getter for _main_model
        """
        return self._main_model

    @property
    def config(self):
        """
        Getter for _config
        """
        return self._config

    @property
    def dicom_parser(self):
        """
        Getter for _dicom_parser
        """
        return self._dicom_parser

    def change_selected_directory(self, dir):
        """
        Check the directory is valid, then update the model
        """
        old_dir = self._main_model.dicom_directory
        if os.path.exists(dir):
            self._main_model.dicom_directory = dir
            self._main_model.image_index = 0
            if not self._dicom_parser.read_directory(dir):
                print(f"{dir} is not a valid file directory")
                self._dicom_parser.read_directory(old_dir)
                return False
            self.update_image_view()
            return True
        else:
            print(f"{dir} is not a valid file directory.")
            return False

    def change_image_index(self, index):
        """
        Update the index of the currently selected image
        """
        num_img = self._dicom_parser.num_images
        if index >= 0 and index < num_img:
            self._main_model.image_index = index
            self.update_image_view()
            return index
        else:
            print(f"Index {index} out of range of dicom images ({num_img})")
            return -1

    def go_to_next_image(self):
        self.change_image_index(self._main_model.image_index + 1)

    def go_to_preivous_image(self):
        self.change_image_index(self._main_model.image_index - 1)

    def default_directory_prompt(self, config, dbfile):
        """
        Prompts the user to supply the default directory
        Updates Config from the DirectoryView
        """
        popup = DirectoryView(config, dbfile)
        popup.exec()

    def check_config(self):
        """
        Checks the Config object and updates _main_model accordingly
        """
        default_dir = self._config().default_dir
        self.change_selected_directory(default_dir)

    def open_image_viewer(self):
        """
        Creates the ImageView popup, replacing the old one if neccessary
        """

        if self._image_popup:
            self._image_popup.close()
        self._image_popup = ImageView(self)
        self._image_popup.show()
        self.update_image_view()

    def update_image_view(self):
        """
        Sets the label and slider of the image view
        as well as updating the image
        """
        if not self._image_popup:
            return False

        # I know the indexing is wrong, but if it's set to anything but these
        # exact values it runs HORRIBLY
        # I could not tell you why
        self._image_popup.slider.setMinimum(1)
        self._image_popup.slider.setMaximum(self._dicom_parser.num_images)
        index = self._main_model.image_index
        # self._image_popup.slider.setValue(index+1)
        title = f"Image {index+1}/{self._dicom_parser.num_images}"
        self._image_popup.update(self._dicom_parser.get_image(index), title)
