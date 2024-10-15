import os, sys
from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import Qt

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler
from views.Components.Imagebox import Imagebox
from views.Components.Dropbox import Dropbox

class Image(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog__item__image")
        self.setObjectName("dialog__item__image")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.dropbox_widget = Dropbox(self)
        self.images_widget = Imagebox({ "class": "item__image__imagebox"}, self)
        self.dropbox_widget.event_dropped_urls.connect(self.set_value)
        main_layout.addWidget(self.dropbox_widget)
        main_layout.addWidget(self.images_widget)
    
    def set_value(self, urls):
        if len(urls) > 0: self.dropbox_widget.hide()
        else: self.dropbox_widget.show()
        self.images_widget.set_value(urls)

    def get_value(self):
        return self.images_widget.get_value()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    img = Image()
    img.show()

    sys.exit(app.exec_())