import os, sys
from PyQt5.QtWidgets import QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from .Store.Store import Store

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from logic.utils.temp_handle import TemplateHandler
from logic.utils.product_handler import ProductHandler

class Pages(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "pages")
        self.setObjectName("pages")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.store_page_widget = Store(self)

        main_layout.addWidget(self.store_page_widget)
    
    def set_page(self, payload):
        page_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "page")
        for page_widget in page_widgets:
            if page_widget.property("user-data") == payload.get("page"): page_widget.show()
            else: page_widget.hide()