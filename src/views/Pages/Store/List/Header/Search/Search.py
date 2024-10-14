import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal

from .SearchBase import SearchBase
from .SearchExpand import SearchExpand

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)

class Search(QFrame):
    event_search_payload = pyqtSignal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "list__header__search")
        self.setObjectName("list__header__search")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.search_payload = {}

        self.search_base_widget = SearchBase(self)
        self.search_base_widget.event_search_base_payload.connect(self.on_search_payload_changed)
        self.search_expand_widget = SearchExpand(self)
        self.search_expand_widget.event_search_expand_payload.connect(self.on_search_payload_changed)

        main_layout.addWidget(self.search_base_widget)
        main_layout.addWidget(self.search_expand_widget)
    
    def set_expand_inputs_widget(self, payload):
        self.search_expand_widget.set_input_widgets(payload)
    
    def on_search_payload_changed(self, e):
        for key in e.keys():
            self.search_payload[key] = e[key]
        _ = []
        for key, value in self.search_payload.items():
            _.append((key, value))
        self.event_search_payload.emit(_)