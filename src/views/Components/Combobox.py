import os, sys
from functools import partial
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QComboBox
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir, ))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Combobox(QFrame):
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
        self.combobox_widget = QComboBox(self)
        self.combobox_widget.currentIndexChanged.connect(lambda e: self.event_current_value.emit(self.get_value()))
        self.combobox_widget.setProperty("class", "combobox")
        main_layout.addWidget(self.combobox_widget)
    
    def showEvent(self, e):
        self.event_current_value.emit(self.get_value())

    def set_options(self, payload):
        self.combobox_widget.clear()
        [{
            "user-data": "",
            "label": ""
        }]
        for index, option in enumerate(payload):
            self.combobox_widget.addItem(option.get("label"))
            self.combobox_widget.setItemData(index, option.get("user-data", Qt.UserRole))

    def set_value(self, payload):
        { "user-data" : ""}
        for i in range(self.combobox_widget.count()):
            for value in payload.values():
                if self.combobox_widget.itemData(i) == value:
                    self.combobox_widget.setCurrentIndex(i)
                    return True
        return False
    
    def get_value(self):
        return {
            self.property("user-data") : self.combobox_widget.currentData()
        }
    
    def remove_items(self):
        while self.combobox_widget.count() > 0:
            self.combobox_widget.removeItem(0)
