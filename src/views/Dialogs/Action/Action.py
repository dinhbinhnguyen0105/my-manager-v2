import os, sys
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Basic(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__action")
        self.setObjectName("dialog__item__action")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.save_btn_widget = QPushButton("Save", self)
        self.save_btn_widget.setProperty("class", "item__action item__action__save")

        main_layout.addWidget(self.save_btn_widget)