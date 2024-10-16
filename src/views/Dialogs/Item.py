import os, sys, datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame, QStackedWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt

from Image.Image import Image
from Options.Options import Options
from Details.Detail import Detail
from Basic.Basic import Basic
from Description.Description import Desciption
from Action.Action import Action

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

        self.data = {}
        self.prev_option = None

        self.options_widget = Options(self)
        self.image_widget = Image(self)
        self.detail_widget = Detail(self)
        self.basic_widget = Basic(self)
        self.description_widget = Desciption(self)
        self.actions_widget = Action(self)

        self.options_widget.event_current_option.connect(self.set_details)
        self.options_widget.event_current_option.connect(self.set_data)
        self.detail_widget.event_current_details.connect(self.set_data)
        self.description_widget.event_current_description.connect(self.set_data)
        self.actions_widget.save_btn_widget.clicked.connect(self.on_save_clicked)

        main_layout.addWidget(self.options_widget)
        main_layout.addWidget(self.image_widget)
        main_layout.addWidget(self.basic_widget)
        main_layout.addWidget(self.detail_widget)
        main_layout.addWidget(self.description_widget)
        main_layout.addWidget(self.actions_widget)
    
    def on_save_clicked(self):
        print(self.data)
    
    def set_data(self, payload):
        self.data = {
            **self.data,
            **payload
        }
        self.basic_widget.set_value({
            "option": self.data.get("option"),
            "type": self.data.get("type")
        })
    
    def set_details(self, option):
        self.detail_widget.set_detail(option.get("option"))

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    item = Item()
    item.show()
    sys.exit(app.exec_())