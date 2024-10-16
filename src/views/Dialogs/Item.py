import os, sys, datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame, QStackedWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt

from Image.Image import Image
from Options.Options import Options
from Details.Detail import Detail
from Basic.Basic import Basic

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)

class Item(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item")
        self.setObjectName("dialog__item")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.options_widget = Options(self)
        self.image_widget = Image(self)
        self.detail_widget = Detail(self)
        self.basic_widget = Basic(self)
        self.options_widget.event_current_option.connect(self.set_details)
        self.detail_widget.real_estate_widget.type_widget.event_current_type.connect(self.set_basic)

        main_layout.addWidget(self.options_widget)
        main_layout.addWidget(self.image_widget)
        main_layout.addWidget(self.basic_widget)
        main_layout.addWidget(self.detail_widget)

    def set_basic(self):

        pass
    
    def set_details(self, option):
        self.detail_widget.set_detail(option)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    item = Item()
    item.show()
    sys.exit(app.exec_())