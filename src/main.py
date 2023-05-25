"""
Instantiates QApplication class, and execute
"""

import sys
from PySide6.QtWidgets import QApplication

from src.models.main_model import MainModel
from src.views.main_view import MainView
from src.controllers.main_controller import MainController


class App(QApplication):
    """
    Instantiates MVC architecture
    """

    def __init__(self, sys_args) -> None:
        super().__init__(sys_args)
        self.model = MainModel(self)
        self.controller = MainController(self.model, self)
        self.view = MainView(self.controller)
        self.view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
