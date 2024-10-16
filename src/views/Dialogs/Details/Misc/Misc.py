import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Lineedit import Lineedit
from views.Components.Combobox import Combobox

class Misc(QFrame):
    event_payload_changed = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "item__detail__miscelaneous, item__detail")
        self.setObjectName("item__detail__miscelaneous")
        self.setProperty("user-data", "miscellaneous")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.data = {}

        self.title = Lineedit({
            "class": "miscelaneous__title",
            "id": "miscelaneous__title",
            "label": "Title: ",
            "user-data": "title",
        }, self)

        main_layout.addWidget(self.title)
    
    def showEvent(self, e):
        self.event_payload_changed.emit(self.get_value())
    
    def set_data(self):
        pass
    
    def set_value(self, payload):
        if payload.get("title"): self.title.set_value(payload.get("title"))
        self.event_payload_changed.emit(self.get_value())
    
    def get_value(self):
        return {
            "title": self.title.get_value()
        }

