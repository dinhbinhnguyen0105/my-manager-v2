import os
from PyQt5.QtWidgets import  QMainWindow
from PyQt5.QtCore import QSize
from .views.views import View

MY_DIR = os.path.abspath(os.path.dirname(__file__))

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My manager")
        self.setProperty("class", "main-window")
        self.setObjectName("main-window")
        self.resize(QSize(1200, 600))
        self.main_widget = View(self)
        self.setCentralWidget(self.main_widget)

        with open(f"{MY_DIR}/main_window.styles.qss", "r") as f:
            styles = f.read()
        self.setStyleSheet(styles)