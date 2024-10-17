import os, sys
from functools import partial
from PyQt5.QtWidgets import QVBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtGui import QIcon

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
ICONS_DIR = os.path.abspath(os.path.join(ASSETS_DIR, "icons"))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from logic.utils.temp_handle import TemplateHandler
from logic.utils.product_handler import ProductHandler
from views.Components.Radio import Radio

class Sidebar(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "sidebar")
        self.setObjectName("sidebar")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.home_btn_widget = QPushButton(self)
        self.home_btn_widget.setProperty("class", "page-btn page__home")
        self.home_btn_widget.setObjectName("page__home")
        self.home_btn_widget.setProperty("user-data", "home")
        self.home_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "home.svg")))
        self.home_btn_widget.setIconSize(QSize(26, 26))

        self.store_btn_widget = QPushButton(self)
        self.store_btn_widget.setProperty("class", "page-btn page__store activated")
        self.store_btn_widget.setObjectName("page__store")
        self.store_btn_widget.setProperty("user-data", "store")
        self.store_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "store.svg")))
        self.store_btn_widget.setIconSize(QSize(26, 26))

        self.robot_btn_widget = QPushButton(self)
        self.robot_btn_widget.setProperty("class", "page-btn page__robot")
        self.robot_btn_widget.setObjectName("page__robot")
        self.robot_btn_widget.setProperty("user-data", "robot")
        self.robot_btn_widget.setIcon(QIcon(os.path.join(ICONS_DIR, "robot.svg")))
        self.robot_btn_widget.setIconSize(QSize(26, 26))
        
        self.home_btn_widget.clicked.connect(partial(self.on_page_clicked, self.home_btn_widget))
        self.store_btn_widget.clicked.connect(partial(self.on_page_clicked, self.store_btn_widget))
        self.robot_btn_widget.clicked.connect(partial(self.on_page_clicked, self.robot_btn_widget))

        main_layout.addWidget(self.home_btn_widget)
        main_layout.addWidget(self.store_btn_widget)
        main_layout.addWidget(self.robot_btn_widget)
    
    def showEvent(self, e):
        self.on_page_clicked(self.store_btn_widget)
    
    def on_page_clicked(self, current_widget):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "page-btn")
        for option_widget in option_widgets:
            WidgetHandler.remove_class(option_widget, "activated")
        WidgetHandler.add_class(current_widget, "activated")
        self.setStyleSheet(self.styleSheet())
        self.event_current_value.emit(self.get_value())
    
    def get_value(self):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "page-btn")
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                return {
                    "page" : option_widget.property("user-data")
                }
        return {}

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    sidebar = Sidebar()
    sidebar.show()
    sys.exit(app.exec_())