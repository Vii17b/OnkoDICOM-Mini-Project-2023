"""
The UI for the image selector
"""

from PySide6.QtWidgets import QMainWindow


class MainView(QMainWindow):
    """
    Docstring
    """
    def __init__(self, controller, parent=None) -> None:
        super().__init__(parent)
        self._controller = controller
        self._model = self._controller.main_model
