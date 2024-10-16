import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

from .Realestate.Realestate import Realestate
from .Misc.Misc import Misc

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Detail(QFrame):
    event_current_details = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__details")
        self.setObjectName("dialog__item__details")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.real_estate_widget = Realestate(self)
        self.real_estate_widget.event_payload_changed.connect(lambda e: self.event_current_details.emit(e))
        self.miscellaneous_widget = Misc(self)

        
        main_layout.addWidget(self.real_estate_widget)
        main_layout.addWidget(self.miscellaneous_widget)
    
    def showEvent(self, e):
        self.set_detail()
    
    def set_detail(self, option="real-estate"):
        detail_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "item__detail")
        for detail_widget in detail_widgets:
            if detail_widget.property("user-data") == option: detail_widget.show()
            else: detail_widget.hide()
    
    def get_value(self):
        detail_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "item__detail")
        for detail_widget in detail_widgets:
            if detail_widget.isHidden(): continue
            else:
                return detail_widget.get_value()
        
