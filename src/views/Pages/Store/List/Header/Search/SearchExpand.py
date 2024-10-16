import os, sys
from PyQt5.QtWidgets import QGridLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.Components.Lineedit import Lineedit
from views.utils.widget_handler import WidgetHandler

class SearchExpand(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "header__search__expand")
        self.setObjectName("header__search__expand")
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)
    
    def set_input_widgets(self, payload):
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "header__search__input")
        for input_widget in input_widgets:
            input_widget.setParent(None)
            input_widget.deleteLater()
        
        row, col = 0, 0
        for index, widget_info in enumerate(payload):
            input_widget = Lineedit(widget_info, self)
            WidgetHandler.add_class(input_widget, "header__search__input")
            input_widget.event_current_value.connect(
                lambda e: self.event_current_value.emit(self.get_value())
            )
            if index % 4 == 0:
                row += 1
                col = 0
            self.layout().addWidget(input_widget, row, col, 1, 1)
            col += 1
            
    def get_value(self):
        data = {}
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "header__search__input")
        for input_widget in input_widgets:
            data = {
                **data,
                **input_widget.get_value()
            }
        return data
            
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    se = SearchExpand()
    se.set_input_widgets([
        {
            "id": "item__type__assignment",
            "class": "item__type__assignment",
            "user-data": "assignment",
            "label": "assignment".capitalize(),
        },
    ])
    se.show()

    sys.exit(app.exec_())