import os, sys, datetime, random
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.Components.Radio import Radio
from views.Components.Combobox import Combobox
from views.Components.Plaintext import Plaintext
from views.Components.Lineedit import Lineedit
from views.utils.widget_handler import WidgetHandler

class Misc(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "miscellaneous dialog__details")
        self.setProperty("user-data", "miscellaneous")
        self.setObjectName("miscellaneous")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        self.id_widget = QLabel(self)
        self.id_widget.setProperty("class", "id__label")
        self.id_widget.setProperty("user-data", "id")
        self.id_widget.setObjectName("id__label")
        self.set_id()
        self.date_widget = QLabel(self)
        self.date_widget.setProperty("class", "date__label")
        self.date_widget.setProperty("user-data", "date")
        self.date_widget.setObjectName("date__label")
        self.set_date()

        self.title_widget = Lineedit({
            "class": "title__input miscellaneous__item",
            "id" : "title__input",
            "user-data" : "title",
            "label": "title: ".title()
        }, self)
        self.description_widget = Plaintext({
            "class": "description__input miscellaneous__item",
            "id" : "description__input",
            "user-data" : "description",
            "label": "description: ".title()
        }, self)

        main_layout.addWidget(self.date_widget)
        main_layout.addWidget(self.id_widget)
        main_layout.addWidget(self.title_widget)
        main_layout.addWidget(self.description_widget)
    
    def showEvent(self, e):
        # self.set_value([
            
        # ])
        pass

    def set_id(self):
        now = datetime.datetime.now()
        randint = random.randint(0, 100)
        id = f"{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
        self.id_widget.setText(f"RE.{id}".upper())

    def set_date(self,):
        now = datetime.datetime.now()
        date = f"{now.strftime('%m')}-{now.strftime('%d')}-{now.strftime('%y')}"
        self.date_widget.setText(date)

    def set_value(self, payload):
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "miscellaneous__item")
        for obj in payload:
            for index, input_widget in enumerate(input_widgets):
                for key in obj.keys():
                    if input_widget.property("user-data") == key:
                        input_widget.set_value(obj)
                        input_widgets.pop(index)
    
    def get_value(self):
        data = {}
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "miscellaneous__item")
        for input_widget in input_widgets:
            data = {
                **data,
                **input_widget.get_value()
            }
        return {
            **data,
            **{ "id" : self.id_widget.text()},
            **{ "date" : self.date_widget.text()},
            **{ "status": "available"},
        }
