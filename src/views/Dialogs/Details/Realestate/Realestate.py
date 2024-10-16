import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from .Type import Type
from .Location import Location
from .Detail import Detail

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
        self.location_widget = Location(self)
        self.location_widget.event_current_location.connect(self.set_data)
        self.detail_widget = Detail(self)
        self.detail_widget.event_current_detail.connect(self.set_data)

        main_layout.addWidget(self.type_widget)
        main_layout.addWidget(self.location_widget)
        main_layout.addWidget(self.detail_widget)

    def set_data(self, payload):
        self.data = {
            **self.data,
            **payload
        }
        self.event_payload_changed.emit(self.data)
