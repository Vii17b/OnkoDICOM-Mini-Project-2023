"""
Instantiates QApplication class, and execute
"""

import sys
from PySide6.QtCore import QApplication

from models.main_model import MainModel
from views.main_view import MainView
from controllers.main_controller import MainController


class App(QApplication):
    """
    Instantiates MVC architecture
    """
    def __init__(self, sys_args) -> None:
        super().__init__(sys_args)
        self.model = MainModel(self)
        self.controller = MainController(self, self.model)
        self.view = MainView(self, self.controller)
        self.view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())
