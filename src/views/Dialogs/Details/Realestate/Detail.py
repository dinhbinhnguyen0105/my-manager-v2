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

class Detail(QFrame):
    event_current_detail = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "real-estate__detail")
        self.setObjectName("real-estate__detail")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.data = {
            "area": "",
            "construction": "",
            "function": "",
            "furniture": "",
            "legal": "",
            "price": ""
        }

        self.area_widget = Lineedit({
            "class": "real-estate__detail real-estate__detail__area",
            "id": "real-estate__detail__area",
            "user-data": "area",
            "label": "Area: ",
        }, self)
        _ = partial(self.set_data, self.area_widget)
        self.area_widget.lineedit_widget.textChanged.connect(_)
        self.construction_widget = Lineedit({
            "class": "real-estate__detail real-estate__detail__construction",
            "id": "real-estate__detail__construction",
            "user-data": "construction",
            "label": "Construction: ",
        }, self)
        _ = partial(self.set_data, self.construction_widget)
        self.construction_widget.lineedit_widget.textChanged.connect(_)
        self.function_widget = Lineedit({
            "class": "real-estate__detail real-estate__detail__function",
            "id": "real-estate__detail__function",
            "user-data": "function",
            "label": "Function: ",
        }, self)
        _ = partial(self.set_data, self.function_widget)
        self.function_widget.lineedit_widget.textChanged.connect(_)
        self.furniture_widget = Combobox({
            "class": "real-estate__detail real-estate__detail__furniture",
            "id": "real-estate__detail__furniture",
            "user-data": "furniture",
            "label": "Furniture: ",
            "options": [
                ("None", "none"),
                ("Basic", "basic"),
                ("Full", "full"),
            ]
        }, self)
        _ = partial(self.set_data, self.furniture_widget)
        self.furniture_widget.combobox_widget.currentIndexChanged.connect(_)
        self.legal_widget = Combobox({
            "class": "real-estate__detail real-estate__detail__legal",
            "id": "real-estate__detail__legal",
            "user-data": "legal",
            "label": "Legal: ",
            "options": [
                ("Không sổ", "none"),
                ("Sổ nông nghiệp chung", "snnc"),
                ("Sổ nông nghiệp phân quyền", "snnpq"),
                ("Sổ nông nghiệp riêng", "srnn"),
                ("Sổ xây dựng chung", "sxdc"),
                ("Sổ xây dựng phân quyền", "sxdpq"),
                ("Sổ xây dựng riêng", "srxd"),
            ]
        }, self)
        _ = partial(self.set_data, self.legal_widget)
        self.legal_widget.combobox_widget.currentIndexChanged.connect(_)
        self.price_widget = Lineedit({
            "class": "real-estate__detail real-estate__detail__price",
            "id": "real-estate__detail__price",
            "user-data": "price",
            "label": "Price: ",
        }, self)
        _ = partial(self.set_data, self.price_widget)
        self.price_widget.lineedit_widget.textChanged.connect(_)

        main_layout.addWidget(self.area_widget, 0, 0, 1, 1)
        main_layout.addWidget(self.construction_widget, 0, 1, 1, 1)
        main_layout.addWidget(self.function_widget, 1, 0, 1, 1)
        main_layout.addWidget(self.furniture_widget, 1, 1, 1, 1)
        main_layout.addWidget(self.legal_widget, 2, 0, 1, 1)
        main_layout.addWidget(self.price_widget, 2, 1, 1, 1)
    
    def showEvent(self, e):
        self.event_current_detail.emit(self.data)
    
    def set_data(self, current_widget):
        self.data = {
            **self.data,
            **{ current_widget.property("user-data") : current_widget.get_value()}
        }
        self.event_current_detail.emit(self.data)
    
    def get_value(self):
        pattern = r"^[0-9.]+$"
        if re.match(pattern, self.price_widget.get_value()): price = float(self.price_widget.get_value())
        else: price = False
        if re.match(pattern, self.area_widget.get_value()): area = float(self.area_widget.get_value())
        else: area = False
        return {
            "area" : area,
            "construction" : self.construction_widget.get_value(),
            "function" : self.function_widget.get_value(),
            "furniture" : self.furniture_widget.get_value(),
            "legal" : self.legal_widget.get_value(),
            "price" : price,
        }

    def set_value(self, payload):
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "real-estate__detail")
        for obj in payload:
            for input_widget in input_widgets:
                user_data = input_widget.property("user-data")
                if obj.get("user-data") == user_data:
                    input_widget.set_value(obj.get("value"))
        return True

class CustomError(Exception):
    pass

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    detail = Detail()
    detail.show()
    detail.set_value([
        { "user-data": "area", "value": "100" },
        { "user-data": "contruction", "value": "3 lau" },
        { "user-data": "legal", "value": "snnc" },
        { "user-data": "furniture", "value": "none" },
    ])
    sys.exit(app.exec_())