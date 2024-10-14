import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from logic.utils.product_handler import ProductHandler
from views.Components.Table import Table

class Body(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list__body")
        self.setObjectName("store__list__body")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.table = Table({
            "class": "store__list__table",
            "id": "store__list__table",
        }, self)
        main_layout.addWidget(self.table)
    
    def set_table(self, option):
        data = ProductHandler.read(option)
        if option == "real-estate":
            headers = [
                ("date", "Date"),
                ("id", "ID"),
                ("type", "Type"),
                ("ward", "Ward"),
                ("street", "Street"),
                ("category", "Category"),
                ("area", "Area"),
                ("price", "Price"),
                ("building_line", "Building line"),
                ("function", "Function"),
                ("furniture", "Furniture"),
                ("legal", "Legal"),
            ]
        elif option == "miscellaneous":
            headers = [
                ("id", "ID"),
                ("title", "title"),
                ("description", "description")
            ]
        else: raise CustomError("Invalid option")
        self.table.set_model({
            "headers": headers,
            "data": data
        })

class CustomError(Exception):
    pass