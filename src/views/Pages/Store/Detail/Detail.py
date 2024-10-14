import os
from PyQt5.QtWidgets import QVBoxLayout, QFrame
from PyQt5.QtCore import Qt

from .Header.Header import Header
from .Body.Body import Body
from .Footer.Footer import Footer
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))


class Detail(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__detail")
        self.setObjectName("store__detail")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.header_widget = Header(self)
        self.body_widget = Body(self)
        self.footer_widget = Footer(self)

        main_layout.addWidget(self.header_widget)
        main_layout.addWidget(self.body_widget)
        main_layout.addWidget(self.footer_widget)

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    detail = Detail()    

    detail.body_widget.set_data({
        "images": ["/Users/ndb/Workspace/mymanager/bin/data/products/images/20240307221620/20240307221620_0.png", "/Users/ndb/Workspace/mymanager/bin/data/products/images/20240327113705/20240327113705_0.png",],
        "title": "title_1",
        "description": "description_1",
    })
    detail.show()

    sys.exit(app.exec_())