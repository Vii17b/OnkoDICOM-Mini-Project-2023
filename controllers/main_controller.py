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
        self._dicom_parser = DicomParser(self._config.default_dir)

        # views
        self._image_popup = None

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
        if os.path.exists(dir):
            # TODO: Update with actual variable names
            # once main model is implemented
            self._main_model.REPLACE_LATER = dir
            self._main_model.REPLACE_LATER = 0
            self._dicom_parser.read_directory(dir)
            return True
        else:
            print(f"{dir} is not a valid file directory.")
            return False

    def change_image_index(self, index):
        """
        Update the index of the currently selected image
        """
        num_img = self._dicom_parser.num_images
        if index > 0 and index < num_img:
            # TODO: Update with actual variable name
            # once main model is implemented
            self._main_model.REPLACE_LATER = index
            return index
        else:
            print(f"Index {index} out of range of dicom images ({num_img})")
            return -1

    def go_to_next_image(self):
        # TODO: Update with actual variable name
        # once main model is implemented
        self.change_image_index(self._main_model.REPLACE_LATER+1)

    def go_to_preivous_image(self):
        # TODO: Update with actual variable name
        # once main model is implemented
        self.change_image_index(self._main_model.REPLACE_LATER-1)

    def default_directory_prompt(self):
        """
        Prompts the user to supply the default directory
        Updates Config from the DirectoryView
        """
        popup = DirectoryView(self)
        popup.exec()

    def check_config(self):
        """
        Checks the Config object and updates _main_model accordingly
        """
        default_dir = self._config().default_dir
        self.change_selected_directory(default_dir)

    def open_image_viewer(self):
        """
        Creates the ImageView popup if it doesn't exist already
        """

        if not self._image_popup:
            self._image_popup = ImageView()
            self._image_popup.show()

    def update_image_view(self):
        """
        Sets the label and slider of the image view
        as well as updating the image
        """
        if not self._image_popup:
            return False

        # TODO: Update with actual variable name
        # once main_model is implemented
        self._image_popup.slider.setMinimum(1)
        self._image_popup.slider.setMaximum(self._dicom_parser.num_images)
        index = self._main_model.REPLACE_LATER
        self._image_popup.slider.value = index+1
        title = f"Image {index+1}/{self._dicom_parser.num_images}"
        self._image_popup.update(self._dicom_parser.get_image(index), title)
