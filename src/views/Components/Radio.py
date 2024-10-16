import os, sys
from functools import partial
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame,  QHBoxLayout, QLabel, QPushButton
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir, ))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Radio(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if payload.get("class"): self.setProperty("class", payload.get("class"))
        if payload.get("id"): self.setObjectName(payload.get("id"))
        if payload.get("user-data"): self.setProperty("user-data", payload.get("user-data"))
        
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        if payload.get("label"):
            label = QLabel(payload.get("label"), self)
            label.setProperty("class", "label")
            main_layout.addWidget(label)
    
    # def showEvent(self, e):
    #     self.event_current_value.emit(self.get_value())
    
    def set_options(self, payload):
        for index, radio in enumerate(payload):
            radio_widget = QPushButton(self)
            if radio.get("id"): radio_widget.setObjectName(radio.get("id"))
            radio_widget.setProperty("class", "radio__option")
            if radio.get("class"): WidgetHandler.add_class(radio_widget, radio.get("class"))
            if index == 0: WidgetHandler.add_class(radio_widget, "activated")
            if radio.get("user-data"): radio_widget.setProperty("user-data", radio.get("user-data"))
            if radio.get("label"): radio_widget.setText(radio.get("label"))
            _ = partial(self.on_option_clicked, radio_widget)
            radio_widget.clicked.connect(_)
            self.layout().addWidget(radio_widget)       
    
    def on_option_clicked(self, current_widget):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "radio__option")
        for option_widget in option_widgets:
            WidgetHandler.remove_class(option_widget, "activated")
        WidgetHandler.add_class(current_widget, "activated")
        self.setStyleSheet(self.styleSheet())
        self.event_current_value.emit(self.get_value())
    
    def set_value(self, payload):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "radio__option")
        for option_widget in option_widgets:
            for value in payload.values():
                if value == option_widget.property("user-data"):
                    WidgetHandler.add_class(option_widget, "activated")
                    self.setStyleSheet(self.styleSheet())
                    self.event_current_value.emit(self.get_value())
                    return True
        return False
    
    def get_value(self):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "radio__option")
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                return {
                    self.property("user-data") : option_widget.property("user-data")
                }
        return {}

class CustomError(Exception):
    pass