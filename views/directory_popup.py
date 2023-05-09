"""
First time popup if the Config cannot find the hidden file
Updates the Config accordingly
"""

from PySide6.QtWidgets import QWidget


class Popup(QWidget):
    """
    Popup view that prompts the user to supply a default directory
    """
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
