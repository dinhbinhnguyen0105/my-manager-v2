import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal

from .SearchBase import SearchBase
from .SearchExpand import SearchExpand

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)

from views.utils.widget_handler import WidgetHandler

class Search(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "list__header__search")
        self.setObjectName("list__header__search")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.data = {}

        self.search_base_widget = SearchBase(self)
        self.search_base_widget.event_current_value.connect(self.set_data)
        self.search_base_widget.expand_btn_widget.clicked.connect(self.set_expand)
        self.search_expand_widget = SearchExpand(self)
        self.search_expand_widget.event_current_value.connect(self.set_data)

        main_layout.addWidget(self.search_base_widget)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.search_expand_widget)
    
    def set_data(self, payload):
        self.data = {
            **self.data,
            **payload
        }
        self.event_current_value.emit(self.data)
        return self.data
       
    
    def get_value(self):
        data = {}
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "header__search__input")
        for input_widget in input_widgets:
            data = {
                **data,
                **input_widget.get_value()
            }
        return data
    
    def set_expand(self):
        if self.search_expand_widget.isHidden(): self.search_expand_widget.show()
        else: self.search_expand_widget.hide()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    sb = Search()
    sb.show()

    sys.exit(app.exec_())