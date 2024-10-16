import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Plaintext import Plaintext

class Desciption(QFrame):
    event_current_description = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__desciption")
        self.setObjectName("dialog__item__desciption")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
        self.data = { "description": "" }

        self.description = Plaintext({
            "class": "item__description",
            "label": "Description: "
        })
        self.description.plaintext_widget.textChanged.connect(self.set_data)

        main_layout.addWidget(self.description)
    
    def showEvent(self, a0):
        self.event_current_description.emit(self.data)
    
    def set_data(self):
        self.data = self.get_value()
        self.event_current_description.emit(self.data)
    
    def set_value(self, payload):
        if payload.get("option"): WidgetHandler.add_class(self.description, payload.get("option"))
        if payload.get("value"): self.description.plaintext_widget.setPlainText(payload.get("value"))
    
    def get_value(self,):
        return {
            "description": self.description.plaintext_widget.toPlainText()
        }

