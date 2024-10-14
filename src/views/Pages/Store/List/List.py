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

        self.search_payload = {}

        self.header = Header(self)
        self.body = Body(self)
        self.set_body_table()
        self.header.options_widget.event_option_active_changed.connect(self.set_body_table)
        main_layout.addWidget(self.header)
        main_layout.addWidget(self.body)
    
    def set_body_table(self, option=False):
        if not option: option = self.header.get_value().get("option")
        self.body.set_table(option)
        self.body.table.clear_filter()
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "header__search__input")
        for input_widget in input_widgets:
            _ = partial(self.set_search_payload, input_widget)
            input_widget.lineedit_widget.setText("")
        self.handle_search_payload_changed()

    def handle_search_payload_changed(self):
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "header__search__input")
        for input_widget in input_widgets:
            _ = partial(self.set_search_payload, input_widget)
            input_widget.lineedit_widget.textChanged.connect(_)
    
    def set_search_payload(self, input_widget, e):
        self.search_payload[input_widget.property("user-data")] = e
        _ = []
        for key in self.search_payload.keys():
            _.append((key, self.search_payload[key]))
        self.body.table.filter_table(_)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    _list = List()
    _list.show()

    sys.exit(app.exec_())