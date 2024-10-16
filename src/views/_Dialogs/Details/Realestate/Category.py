import os, sys, re
from functools import partial
from PyQt5.QtWidgets import QFrame, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Lineedit import Lineedit
from views.Components.Combobox import Combobox

class Category(QFrame):
    event_current_category = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "real-estate__category")
        self.setObjectName("real-estate__category")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.data = { "category" : ""}

        self.category_widget = Combobox({
            "class": "real-estate__category real-estate__category",
            "id": "real-estate__category",
            "user-data": "category",
            "label": "Category: ",
        }, self)
        self.category_widget.combobox_widget.currentIndexChanged.connect(self.set_data)

        main_layout.addWidget(self.category_widget)
    
    def set_categories(self, _type):
        if _type == "sell":
            categories = [
                ("House", "house"),
                ("Shophouse", "shophouse"),
                ("Villa", "villa"),
                ("Apartment", "apartment"),
                ("Homestay", "homestay"),
                ("Hotel", "hotel"),
                ("Land", "land"),
            ]
        elif _type == "rent":
            categories = [
                ("House", "house"),
                ("Shophouse", "shophouse"),
                ("Villa", "villa"),
                ("Apartment", "apartment"),
                ("Homestay", "homestay"),
                ("Hotel", "hotel"),
                ("Land", "land"),
                ("Retail space", "retailspace"),
                ("Workshop", "workshop"),
                ("Coffee house", "coffeehouse"),
            ]
        elif _type == "assignment":
            categories = [
                ("Homestay", "homestay"),
                ("Hotel", "hotel"),
                ("Retail space", "retailspace"),
                ("Workshop", "workshop"),
                ("Coffee house", "coffeehouse"),
            ]
        
        self.category_widget.remove_items()
        for category in categories:
            self.category_widget.combobox_widget.addItem(category[0], category[1])
    
    def showEvent(self, e):
        self.event_current_category.emit(self.get_value())

    def set_data(self, e):
        self.event_current_category.emit(self.get_value())

    # def set_value(self, payload):
    #     {}
    #     input_wigets = WidgetHandler.find_widgets_by_class(self, QFrame, "real-estate__category")
    #     for _ in payload:
    #         if not _.get("user-data"): continue
    #         for input_widget in input_wigets:
    #             if input_widget.property("user-data") == _.get("user-data"):
    #                 input_widget.set_value(_)

    def get_value(self,):
        return {
            "category": self.category_widget.get_value()
        }