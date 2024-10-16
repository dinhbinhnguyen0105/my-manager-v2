import os, sys
from functools import partial
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QLineEdit
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir, ))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Lineedit(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if payload.get("class"): self.setProperty("class", payload.get("class"))
        if payload.get("id"): self.setObjectName(payload.get("id"))
        if payload.get("user-data"): self.setProperty("user-data", payload.get("user-data"))
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        if payload.get("label"):
            label = QLabel(payload.get("label"), self)
            label.setProperty("class", "label")
            main_layout.addWidget(label)
        self.input_widget = QLineEdit(self)
        self.input_widget.setProperty("class", "lineedit")
        self.input_widget.textChanged.connect(lambda e: self.event_current_value.emit(self.get_value()))
        if payload.get("place-holder"): self.input_widget.setPlaceholderText(payload.get("place-holder"))
        main_layout.addWidget(self.input_widget)

    def showEvent(self, e):
        self.event_current_value.emit(self.get_value())
    def set_value(self, payload):
        for value in payload.values():
            self.input_widget.setText(value)
    def get_value(self):
        return {
            self.property("user-data") : self.input_widget.text()
        }