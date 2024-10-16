import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from .Type import Type
from .Location import Location
from .Detail import Detail
from .Category import Category

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Lineedit import Lineedit
from views.Components.Combobox import Combobox

class Realestate(QFrame):
    event_payload_changed = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "item__detail__real-estate, item__detail")
        self.setObjectName("item__detail__real-estate")
        self.setProperty("user-data", "real-estate")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.data = {}

        self.type_widget = Type(self)
        self.type_widget.event_current_type.connect(self.set_data)
        self.type_widget.event_current_type.connect(self.on_type_changed)
        self.location_widget = Location(self)
        self.location_widget.event_current_location.connect(self.set_data)
        self.category_widget = Category(self)
        self.category_widget.event_current_category.connect(self.set_data)
        self.category_widget.event_current_category.connect(self.on_category_changed)
        self.detail_widget = Detail(self)
        self.detail_widget.event_current_detail.connect(self.set_data)

        main_layout.addWidget(self.type_widget)
        main_layout.addWidget(self.location_widget)
        main_layout.addWidget(self.category_widget)
        main_layout.addWidget(self.detail_widget)
    
    def on_type_changed(self, payload):
        _type = payload.get("type")
        self.category_widget.set_categories(_type)
        if _type == "sell":
            self.detail_widget.area_widget.set_value("")
            self.detail_widget.legal_widget.set_value("none")
            self.detail_widget.area_widget.setEnabled(True)
            self.detail_widget.legal_widget.setEnabled(True)
        elif _type == "rent" or _type == "assignment":
            self.detail_widget.area_widget.setEnabled(False)
            self.detail_widget.legal_widget.setEnabled(False)
    
    def on_category_changed(self, payload):
        category = payload.get("category")
        if category == "apartment" or\
            category == "retailspace" or\
            category == "workshop":
            self.detail_widget.construction_widget.set_value("")
            self.detail_widget.construction_widget.setEnabled(False)
            self.detail_widget.function_widget.setEnabled(True)
            self.detail_widget.furniture_widget.setEnabled(True)
        elif category == "land":
            self.detail_widget.construction_widget.set_value("")
            self.detail_widget.construction_widget.setEnabled(False)
            self.detail_widget.function_widget.set_value("")
            self.detail_widget.function_widget.setEnabled(False)
            self.detail_widget.furniture_widget.setEnabled(False)
        else:
            self.detail_widget.construction_widget.set_value("")
            self.detail_widget.construction_widget.setEnabled(True)
            self.detail_widget.function_widget.setEnabled(True)
            self.detail_widget.furniture_widget.setEnabled(True)
        
    def set_data(self, payload):
        self.data = {
            **self.data,
            **payload
        }
        self.event_payload_changed.emit(self.data)
