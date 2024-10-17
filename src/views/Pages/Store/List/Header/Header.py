import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal

from .Options.Options import Options
from .Search.Search import Search

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from logic.utils.file_handler import FileHandler
from views.utils.widget_handler import WidgetHandler

class Header(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list__header")
        self.setObjectName("store__list__header")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.data = {}
        
        self.options_widget = Options(self)
        self.options_widget.event_current_value.connect(self.on_options_changed)
        self.search_widget = Search(self)
        self.search_widget.event_current_value.connect(self.set_data)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(self.options_widget)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.search_widget)

    def set_data(self, payload):
        self.data = {
            **self.options_widget.get_value(),
            **self.data,
            **payload
        }
        self.event_current_value.emit(self.data)
        return self.data
    
    def get_value(self):
        return {
            **self.options_widget.get_value(),
            **self.data,
        }

    def on_options_changed(self, payload):
        if payload.get("options") == "real-estate":
            input_widget_info = [
                {
                    "id": "header__search__date",
                    "class": "header__search__date header__search__input",
                    "label": "date: ".capitalize(),
                    "user-data": "date"
                },
                {
                    "id": "header__search__type",
                    "class": "header__search__type header__search__input",
                    "label": "type: ".capitalize(),
                    "user-data": "type"
                },
                {
                    "id": "header__search__ward",
                    "class": "header__search__ward header__search__input",
                    "label": "ward: ".capitalize(),
                    "user-data": "ward"
                },
                {
                    "id": "header__search__street",
                    "class": "header__search__street header__search__input",
                    "label": "street: ".capitalize(),
                    "user-data": "street"
                },
                {
                    "id": "header__search__category",
                    "class": "header__search__category header__search__input",
                    "label": "category: ".capitalize(),
                    "user-data": "category"
                },
                {
                    "id": "header__search__area",
                    "class": "header__search__area header__search__input",
                    "label": "area: ".capitalize(),
                    "user-data": "area"
                },
                {
                    "id": "header__search__buildingline",
                    "class": "header__search__buildingline header__search__input",
                    "label": "building line: ".capitalize(),
                    "user-data": "buildingline"
                },
                {
                    "id": "header__search__function",
                    "class": "header__search__function header__search__input",
                    "label": "function: ".capitalize(),
                    "user-data": "function"
                },
                {
                    "id": "header__search__legal",
                    "class": "header__search__legal header__search__input",
                    "label": "legal: ".capitalize(),
                    "user-data": "legal"
                },
                {
                    "id": "header__search__price",
                    "class": "header__search__price header__search__input",
                    "label": "price: ".capitalize(),
                    "user-data": "price"
                }
            ]
        elif payload.get("options") == "miscellaneous":
            input_widget_info = [
                {
                    "id": "header__search__title",
                    "class": "header__search__title header__search__input",
                    "label": "title: ".capitalize(),
                    "user-data": "title"
                },
                {
                    "id": "header__search__desciption",
                    "class": "header__search__desciption header__search__input",
                    "label": "desciption: ".capitalize(),
                    "user-data": "desciption"
                },
            ]
        else: raise CustomError("Invalid option")
        self.search_widget.search_expand_widget.set_input_widgets(input_widget_info)

class CustomError(Exception):
    pass

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    sb = Header()
    sb.event_current_value.connect(lambda e: print(e))
    sb.show()

    sys.exit(app.exec_())