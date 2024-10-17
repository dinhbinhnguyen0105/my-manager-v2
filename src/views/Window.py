import os
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout
from PyQt5.QtCore import QSize
from .Views import Views
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir))

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My manager")
        self.setProperty("class", "main-window")
        self.setObjectName("main-window")
        self.resize(QSize(1200, 600))

        self.main_widget = Views(self)
        self.setCentralWidget(self.main_widget)

        with open(os.path.abspath(os.path.join(MY_DIR, "main.styles.qss")), "r") as f:
            styles = f.read()
        self.setStyleSheet(styles)