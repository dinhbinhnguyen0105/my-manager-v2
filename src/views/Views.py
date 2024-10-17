import os, sys
from PyQt5.QtWidgets import QFrame, QHBoxLayout
from PyQt5.QtCore import QSize, pyqtSignal, Qt
from .Sidebar.Sidebar import Sidebar
from .Pages.Pages import Pages

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
ICONS_DIR = os.path.abspath(os.path.join(ASSETS_DIR, "icons"))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from logic.utils.temp_handle import TemplateHandler
from logic.utils.product_handler import ProductHandler
from views.Components.Radio import Radio

class Views(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "views")
        self.setObjectName("views")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignLeft)

        self.sidebar = Sidebar(self)
        self.sidebar.event_current_value.connect(self.on_page_btn_changed)
        self.pages = Pages(self)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.pages)
    
    def on_page_btn_changed(self, e):
        self.pages.set_page(e)