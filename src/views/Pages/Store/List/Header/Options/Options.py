import os, sys
from functools import partial
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Options(QFrame):
    event_option_active_changed = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "list__header__options")
        self.setObjectName("list__header__options")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
    
    def set_options(self, payload):
        for option_payload in payload:
            option_widget = QPushButton(self)
            if "id" in option_payload.keys():
                self.id = option_payload.get("id")
                option_widget.setObjectName(self.id)
            if "class" in option_payload.keys():
                self._class = option_payload.get("class")
                option_widget.setProperty("class", self._class)
            if "user-data" in option_payload.keys():
                self.user_data = option_payload.get("user-data")
                option_widget.setProperty("user-data", self.user_data)
            if "label" in option_payload.keys():
                self.label = option_payload.get("label")
                option_widget.setText(self.label)
            click_handler = partial(self.on_option_clicked, option_widget)
            option_widget.clicked.connect(click_handler)
            self.layout().addWidget(option_widget)

    def set_event_for_option_widget(self, option_widget):
        self.on_option_clicked(option_widget)

    def set_value(self, index=0):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, self._class)
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                WidgetHandler.remove_class("activated")
        WidgetHandler.add_class(option_widgets[index], "activated")
        self.event_option_active_changed.emit(option_widgets[index].property("user-data"))

    def get_value(self):
        activated_option_widget = WidgetHandler.find_widgets_by_class(self, QPushButton, "activated")[0]
        return activated_option_widget.property("user-data")

    def on_option_clicked(self, clicked_option_widget):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, self._class)
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                WidgetHandler.remove_class(option_widget, "activated")
                break
        WidgetHandler.add_class(clicked_option_widget, "activated")
        self.event_option_active_changed.emit(clicked_option_widget.property("user-data"))
