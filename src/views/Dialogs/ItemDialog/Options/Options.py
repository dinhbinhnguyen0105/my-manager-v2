import os, sys
from PyQt5.QtWidgets import QFrame, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.Components.Radio import Radio
from views.utils.widget_handler import WidgetHandler

class Options(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__options")
        self.setObjectName("dialog__item__options")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.options_widget = Radio({
            "class": "options__input",
            "id" : "options__input",
            "user-data" : "options",
            # "label": "Options"
        }, self)
        self.options_widget.event_current_value.connect(self.on_option_changed)
        main_layout.addWidget(self.options_widget)
        self.set_options()
    
    def on_option_changed(self, e):
        self.event_current_value.emit(e)

    def showEvent(self, e):
        self.set_value({ "options": "real-estate" })
        self.event_current_value.emit(self.get_value())

    def set_value(self, payload):
        self.options_widget.set_value(payload)

    def get_value(self):
        return self.options_widget.get_value()

    def set_options(self):
        self.options_widget.set_options([
            {
                "id": "item__option__real-estate",
                "class": "item__option__real-estate item__option",
                "user-data": "real-estate",
                "label": "real estate".capitalize(),
            },
            {
                "id": "item__option__miscellaneous",
                "class": "item__option__miscellaneous item__option",
                "user-data": "miscellaneous",
                "label": "misc".capitalize(),
            },
            {
                "id": "item__option__food",
                "class": "item__option__food item__option",
                "user-data": "food",
                "label": "food".capitalize(),
            },
            {
                "id": "item__option__travel",
                "class": "item__option__travel item__option",
                "user-data": "travel",
                "label": "travel".capitalize(),
            },
            {
                "id": "item__option__fashion",
                "class": "item__option__fashion item__option",
                "user-data": "fashion",
                "label": "fashion".capitalize(),
            },
        ])