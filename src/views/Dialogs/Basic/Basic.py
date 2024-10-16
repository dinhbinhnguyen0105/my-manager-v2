import os, sys, datetime, random
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Basic(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__basic")
        self.setObjectName("dialog__item__basic")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.date_widget = QLabel(self)
        self.date_widget.setProperty("class", "item__basic__date")
        self.id_widget = QLabel(self)
        self.id_widget.setProperty("class", "item__basic__id")

        main_layout.addWidget(self.date_widget)
        main_layout.addWidget(self.id_widget)

    def set_value(self, payload):
        now = datetime.datetime.now()
        if "option" in payload.keys() and "type" in payload.keys():
            randint = random.randint(0, 100)
            date = f"{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
            if payload["option"] == "real-estate": option = "RE"
            elif payload["option"] == "fashion": option = "FASHION"
            elif payload["option"] == "food": option = "FOOD"
            elif payload["option"] == "travel": option = "TRAVEL"
            elif payload["option"] == "miscellaneous": option = "MISC"
            self.id_widget.setText(f"{option}.{payload['type']}.{date}".upper())
        else: raise CustomError("invalid option or type")

        date = f"{now.strftime('%m')}-{now.strftime('%d')}-{now.strftime('%y')}"
        self.date_widget.setText(date)

    def get_value(self):
        return {
            "date": self.date_widget.text(),
            "id": self.id.text(),
        }

class CustomError(Exception):
    pass