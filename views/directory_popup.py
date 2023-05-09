"""
First time popup if the Config cannot find the hidden file
Updates the Config accordingly
"""

from PySide6.QtWidgets import QDialog


class Popup(QDialog):
    """
    Popup view that prompts the user to supply a default directory
    """
    def __init__(self, main_controller, parent=None) -> None:
        super().__init__(parent)

        self._main_controller = main_controller
