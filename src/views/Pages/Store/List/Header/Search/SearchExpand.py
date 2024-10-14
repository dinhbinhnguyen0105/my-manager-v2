import os, sys
from PyQt5.QtWidgets import QGridLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.Components.Lineedit import Lineedit
from views.utils.widget_handler import WidgetHandler

class SearchExpand(QFrame):
    event_search_expand_payload = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "header__search__expand")
        self.setObjectName("header__search__expand")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.input_widgets = []
    
    def set_input_widgets(self, payload):
        input_widgets = self.findChildren(Lineedit)
        for input_widget in input_widgets:
            input_widget.setParent(None)
            input_widget.deleteLater()
        row = 0
        col = 0
        for index, input in enumerate(payload):
            input_widget = Lineedit({
                "class": f"header__search__{input[0]} header__search__input",
                "id": f"header__search__{input[0]}",
                "user-data": input[0],
                "label": input[1],
            })
            input_widget.lineedit_widget.textChanged.connect(self.on_text_changed)
            if index % 4 == 0:
                row += 1
                col = 0
            self.layout().addWidget(input_widget, row, col, 1, 1)
            col += 1
            self.input_widgets.append(input_widget)
    
    def on_text_changed(self, e):
        _ = {}
        try:
            for input_widget in self.input_widgets:
                _[input_widget.property("user-data")] = input_widget.get_value()
            self.event_search_expand_payload.emit(_)
        except: pass
        # input_widgets = WidgetHandler.find_widgets_by_class(self, Lineedit, "header__search__input")
        