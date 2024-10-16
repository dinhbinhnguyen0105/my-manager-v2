import os, sys
from functools import partial
from PyQt5.QtWidgets import QFrame, QGridLayout, QComboBox
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Lineedit import Lineedit
from views.Components.Combobox import Combobox

PROVIDE_OPTIONS = [("Lâm Đồng", "lamdong")]
DISTRICT_OPTIONS = [("Đà Lạt", "dalat"), ("Đức Trọng", "ductrong")]
WARD_OPTIONS = [
    ("Ward 1", "1"),
    ("Ward 2", "2"),
    ("Ward 3", "3"),
    ("Ward 4", "4"),
    ("Ward 5", "5"),
    ("Ward 6", "6"),
    ("Ward 7", "7"),
    ("Ward 8", "8"),
    ("Ward 9", "9"),
    ("Ward 10", "10"),
    ("Ward 11", "11"),
    ("Ward 12", "12"),
    ("Ward Tà Nung", "tanung"),
    ("Ward Trạm Hành", "tramhanh"),
    ("Ward Xuân Trường", "xuantruong"),
    ("Ward Xuân Thọ", "xuantho"),
]

class Location(QFrame):
    event_current_location = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "real-estate__location")
        self.setObjectName("real-estate__location")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.data = {
            "provide": "lamdong",
            "district": "dalat",
            "ward": "1",
            "street": ""
        }

        self.provide_widget = Combobox({
            "class": "real-estate__location real-estate__location__provide",
            "id": "real-estate__location__provide",
            "user-data": "provide",
            "label": "Provide: ",
        }, self)
        self.provide_widget.set_option(PROVIDE_OPTIONS)
        _ = partial(self.set_data, self.provide_widget)
        self.provide_widget.combobox_widget.currentIndexChanged.connect(_)
        self.provide_widget.setDisabled(True)
        self.district_widget = Combobox({
            "class": "real-estate__location real-estate__location__district",
            "id": "real-estate__location__district",
            "user-data": "district",
            "label": "District: ",
        }, self)
        self.district_widget.set_option(DISTRICT_OPTIONS)
        self.district_widget.setDisabled(True)
        _ = partial(self.set_data, self.district_widget)
        self.provide_widget.combobox_widget.currentIndexChanged.connect(_)
        self.ward_widget = Combobox({
            "class": "real-estate__location real-estate__location__ward",
            "id": "real-estate__location__ward",
            "user-data": "ward",
            "label": "Ward: ",
        }, self)
        self.ward_widget.set_option(WARD_OPTIONS)
        _ = partial(self.set_data, self.ward_widget)
        self.provide_widget.combobox_widget.currentIndexChanged.connect(_)
        self.street_widget = Lineedit({
            "class": "real-estate__location real-estate__location__street",
            "id": "real-estate__location__street",
            "user-data": "street",
            "label": "Street: ",
        }, self)
        _ = partial(self.set_data, self.street_widget)
        self.street_widget.lineedit_widget.textChanged.connect(_)
        
        main_layout.addWidget(self.provide_widget, 0, 0, 1, 1)
        main_layout.addWidget(self.district_widget, 0, 1, 1, 3)
        main_layout.addWidget(self.ward_widget, 1, 0, 1, 1)
        main_layout.addWidget(self.street_widget, 1, 1, 1, 3)
    
    def showEvent(self, e):
        self.event_current_location.emit(self.data)
    
    def set_data(self, current_widget):
        self.data = {
            **self.data,
            **{ current_widget.property("user-data") : current_widget.get_value()}
        }
        self.event_current_location.emit(self.data)