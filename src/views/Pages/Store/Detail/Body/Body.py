import os, sys
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.Components.Lineedit import Lineedit
from views.Components.Plaintext import Plaintext
from views.Components.Imagebox import Imagebox


class Body(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__detail__body")
        self.setObjectName("store__detail__body")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.images_widget = Imagebox({
            "class": "detail__body__images",
            "id": "store__detail__images"
        })
        self.images_widget.setFixedSize(300, 200)
        self.title_widget = Lineedit({
            "class": "detail__body__title",
            "id": "store__detail__title"
        })
        self.description_widget = Plaintext({
            "class": "detail__body__description",
            "id": "store__detail__description"
        })

        main_layout.addWidget(self.images_widget)
        main_layout.addWidget(self.title_widget)
        main_layout.addWidget(self.description_widget)
    
    def set_value(self, payload):
        if "images" in payload.keys(): self.images_widget.set_value(payload.get("images"))
        if "title" in payload.keys(): self.title_widget.set_value(payload.get("title"))
        if "description" in payload.keys(): self.description_widget.set_value(payload.get("description"))

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    body = Body()
    body.show()
    sys.exit(app.exec_())