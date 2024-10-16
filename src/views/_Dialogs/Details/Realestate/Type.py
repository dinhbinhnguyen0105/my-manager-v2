import os, sys
from functools import partial
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Lineedit import Lineedit
from views.Components.Combobox import Combobox

class Type(QFrame):
    event_current_type = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "real-estate__type")
        self.setObjectName("real-estate__type")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.type_sell_widget = QPushButton(self)
        self.type_sell_widget.setObjectName("type__sell")
        self.type_sell_widget.setProperty("class", "type__sell real-estate__type__item")
        self.type_sell_widget.setProperty("user-data", "sell")
        self.type_sell_widget.setProperty("option-index", 0)
        self.type_sell_widget.setText("Sell")
        _ = partial(self.on_option_clicked, self.type_sell_widget)
        self.type_sell_widget.clicked.connect(_)
        
        self.type_rent_widget = QPushButton(self)
        self.type_rent_widget.setObjectName("type__rent")
        self.type_rent_widget.setProperty("class", "type__rent real-estate__type__item")
        self.type_rent_widget.setProperty("user-data", "rent")
        self.type_rent_widget.setProperty("option-index", 1)
        self.type_rent_widget.setText("Rent")
        _ = partial(self.on_option_clicked, self.type_rent_widget)
        self.type_rent_widget.clicked.connect(_)
        
        self.type_assignment_widget = QPushButton(self)
        self.type_assignment_widget.setObjectName("option__assignment")
        self.type_assignment_widget.setProperty("class", "option__assignment real-estate__type__item")
        self.type_assignment_widget.setProperty("user-data", "assignment")
        self.type_assignment_widget.setProperty("option-index", 2)
        self.type_assignment_widget.setText("Assignment")
        _ = partial(self.on_option_clicked, self.type_assignment_widget)
        self.type_assignment_widget.clicked.connect(_)

        main_layout.addWidget(self.type_sell_widget)
        main_layout.addWidget(self.type_rent_widget)
        main_layout.addWidget(self.type_assignment_widget)
    
    def showEvent(self, e):
        self.set_value()

    def set_value(self, option="sell"):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "real-estate__type__item")
        for option_widget in option_widgets:
            if option_widget.property("user-data") == option:
                WidgetHandler.add_class(option_widget, "activated")
                self.event_current_type.emit({ "type": option})
                return True
            
    def on_option_clicked(self, current_widget):
        activated_button_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            WidgetHandler.remove_class(activated_button_widgets[0], "activated")
        WidgetHandler.add_class(current_widget, "activated")
        self.event_current_type.emit({ "type": current_widget.property("user-data")})
        self.setStyleSheet(self.styleSheet())
    
    def get_value(self):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "real-estate__type__item")
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                return option_widget.property("user-data")
        raise CustomError("Invalid user-data")

class CustomError(Exception):
    pass