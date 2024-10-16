import os, sys
from functools import partial
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Options(QFrame):
    event_current_option = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__options")
        self.setObjectName("dialog__item__options")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.option_re_widget = QPushButton(self)
        self.option_re_widget.setObjectName("option__re")
        self.option_re_widget.setProperty("class", "option__re dialog__item__option")
        self.option_re_widget.setProperty("user-data", "real-estate")
        self.option_re_widget.setProperty("option-index", 0)
        self.option_re_widget.setText("Real estate")
        _ = partial(self.on_option_clicked, self.option_re_widget)
        self.option_re_widget.clicked.connect(_)
        
        self.option_fashion_widget = QPushButton(self)
        self.option_fashion_widget.setObjectName("option__fashion")
        self.option_fashion_widget.setProperty("class", "option__fashion dialog__item__option")
        self.option_fashion_widget.setProperty("user-data", "fashion")
        self.option_fashion_widget.setProperty("option-index", 1)
        self.option_fashion_widget.setText("Fashion")
        _ = partial(self.on_option_clicked, self.option_fashion_widget)
        self.option_fashion_widget.clicked.connect(_)
        
        self.option_food_widget = QPushButton(self)
        self.option_food_widget.setObjectName("option__food")
        self.option_food_widget.setProperty("class", "option__food dialog__item__option")
        self.option_food_widget.setProperty("user-data", "food")
        self.option_food_widget.setProperty("option-index", 2)
        self.option_food_widget.setText("Food")
        _ = partial(self.on_option_clicked, self.option_food_widget)
        self.option_food_widget.clicked.connect(_)
        
        self.option_travel_widget = QPushButton(self)
        self.option_travel_widget.setObjectName("option__travel")
        self.option_travel_widget.setProperty("class", "option__travel dialog__item__option")
        self.option_travel_widget.setProperty("user-data", "travel")
        self.option_travel_widget.setProperty("option-index", 0)
        self.option_travel_widget.setText("Travel")
        _ = partial(self.on_option_clicked, self.option_travel_widget)
        self.option_travel_widget.clicked.connect(_)
        
        self.option_misc_widget = QPushButton(self)
        self.option_misc_widget.setObjectName("option__misc")
        self.option_misc_widget.setProperty("class", "option__misc dialog__item__option")
        self.option_misc_widget.setProperty("user-data", "miscellaneous")
        self.option_misc_widget.setProperty("option-index", 3)
        self.option_misc_widget.setText("Misc")
        _ = partial(self.on_option_clicked, self.option_misc_widget)
        self.option_misc_widget.clicked.connect(_)

        main_layout.addWidget(self.option_re_widget)
        main_layout.addWidget(self.option_fashion_widget)
        main_layout.addWidget(self.option_food_widget)
        main_layout.addWidget(self.option_travel_widget)
        main_layout.addWidget(self.option_misc_widget)

    def showEvent(self, e):
        self.set_value()

    def set_value(self, option="real-estate"):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "dialog__item__option")
        for option_widget in option_widgets:
            if option_widget.property("user-data") == option:
                WidgetHandler.add_class(option_widget, "activated")
                self.event_current_option.emit({ "option": option})
                return True
            
    def on_option_clicked(self, current_widget):
        activated_button_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "activated")
        if activated_button_widgets:
            WidgetHandler.remove_class(activated_button_widgets[0], "activated")
        WidgetHandler.add_class(current_widget, "activated")
        self.event_current_option.emit({ "option": current_widget.property("user-data")})
        self.setStyleSheet(self.styleSheet())
    
    def get_value(self):
        option_widgets = WidgetHandler.find_widgets_by_class(self, QPushButton, "content__option")
        for option_widget in option_widgets:
            if "activated" in option_widget.property("class"):
                return option_widget.property("user-data")
        raise CustomError("Invalid user-data")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    option = Options()
    option.show()
    sys.exit(app.exec_())

class CustomError(Exception):
    pass