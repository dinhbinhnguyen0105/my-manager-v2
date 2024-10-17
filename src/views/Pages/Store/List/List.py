import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from functools import partial

from .Header.Header import Header
from .Body.Body import Body

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)

from views.utils.widget_handler import WidgetHandler
from logic.utils.product_handler import ProductHandler

class List(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list")
        self.setObjectName("store__list")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.filter_payload = {}

        self.header = Header(self)
        self.body = Body(self)
        self.header.options_widget.event_current_value.connect(self.on_options_changed)
        main_layout.addWidget(self.header)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.body)
    
    def on_options_changed(self, payload):
        if payload.get("options") == "real-estate":
            headers = [
                { "user-data" : "date" , "label" : "Date"},
                { "user-data" : "id" , "label" : "ID"},
                { "user-data" : "type" , "label" : "Type"},
                { "user-data" : "ward" , "label" : "Ward"},
                { "user-data" : "street" , "label" : "Street"},
                { "user-data" : "categories" , "label" : "Category"},
                { "user-data" : "area" , "label" : "Area"},
                { "user-data" : "price" , "label" : "Price"},
                { "user-data" : "buildingline" , "label" : "Building line"},
                { "user-data" : "function" , "label" : "Function"},
                { "user-data" : "furniture" , "label" : "Furniture"},
                { "user-data" : "legal" , "label" : "Legal"},
            ]
        elif payload.get("options") == "miscellaneous":
            headers = [
                { "user-data" : "id" , "label" : "ID"},
                { "user-data" : "title" , "label" : "title"},
                { "user-data" : "description" , "label" : "description"},
            ]
        else: raise CustomError("Invalid option")
        data = ProductHandler.read(payload.get("options"))

        self.body.table.set_model({ "headers" : headers, "data" : data })
        self.body.table.clear_filter()

        self.filter_payload = {}
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "header__search__input")
        for input_widget in input_widgets:
            input_widget.event_current_value.connect(self.set_filter_payload)
    
    def set_filter_payload(self, payload):
        self.filter_payload = {
            **self.filter_payload,
            **payload
        }
        list_of_filter = []
        for key, value in self.filter_payload.items():
            list_of_filter.append({ key : value})        
        self.body.table.filter_table(list_of_filter)
    

class CustomError(Exception):
    pass

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    _list = List()
    _list.show()

    sys.exit(app.exec_())