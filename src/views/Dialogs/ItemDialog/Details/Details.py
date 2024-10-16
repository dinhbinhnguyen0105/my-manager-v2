import os, sys
from PyQt5.QtWidgets import QFrame, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

from .Misc import Misc
from .RealEstate import RealEstate

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.Components.Radio import Radio
from views.utils.widget_handler import WidgetHandler

class Details(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__details")
        self.setObjectName("dialog__item__details")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.misc_widget = Misc(self)
        WidgetHandler.add_class(self.misc_widget, "item__details")
        self.real_estate_widget = RealEstate(self)
        WidgetHandler.add_class(self.real_estate_widget, "item__details")

        main_layout.addWidget(self.misc_widget)
        main_layout.addWidget(self.real_estate_widget)
    
    # def showEvent(self, e):
    #     detail_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "item__details")
    #     for detail_widget in detail_widgets:
    #         detail_widget.hide()

    def get_value(self):
        detail_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "item__details")
        for detail_widget in detail_widgets:
            if detail_widget.isHidden(): continue
            return detail_widget.get_value()
    
    def set_value(self, payload):
        
        pass