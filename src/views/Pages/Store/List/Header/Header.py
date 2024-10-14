import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

from .Options.Options import Options
from .Search.Search import Search

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from logic.utils.file_handler import FileHandler

class Header(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__list__header")
        self.setObjectName("store__list__header")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
        self.option = False
        self.options_widget = Options(self)
        self.set_option_widget()
        self.search_widget = Search(self)
        self.set_expand_input_widget(self.option)
        self.options_widget.event_option_active_changed.connect(self.set_expand_input_widget)
        

        main_layout.addWidget(self.options_widget)
        main_layout.addWidget(self.search_widget)
    
    def set_expand_input_widget(self, option):
        if option == "real-estate":
            headers = [
                ("date", "Date"),
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
                ("title", "title"),
                ("description", "description")
            ]
        else: raise CustomError("Invalid option")

        self.search_widget.set_expand_inputs_widget(headers)
    
    def set_option_widget(self):
        names_of_data = FileHandler.get_file_names_of_data()
        options = []
        for name_of_data in names_of_data:
            if name_of_data == "real-estate": name = "real estate"
            elif name_of_data == "miscellaneous": name = "miscellaneous"
            options.append({
                "id": f"header__option__{name_of_data}",
                "class": "header__option",
                "user-data": f"{name_of_data}",
                "label": name
            })
        self.options_widget.set_options(options)
        self.options_widget.set_value(0)
        self.option = self.options_widget.get_value()

    def get_value(self):
        return {
            "option": self.option
        }

class CustomError(Exception):
    pass

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    header = Header()
    header.show()

    sys.exit(app.exec_())