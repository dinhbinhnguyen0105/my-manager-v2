import os, sys
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.Components.Lineedit import Lineedit

class SearchBase(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "header__search__base")
        self.setObjectName("header__search__base")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignCenter)

        self.id_input_widget = Lineedit({
            "id": "header__search__id",
            "class": "header__search__id header__search__input",
            "label": "ID: ",
            "user-data": "id"
        })
        self.id_input_widget.event_current_value.connect(lambda e: self.event_current_value.emit(e))

        self.expand_btn_widget = QPushButton(self)
        self.expand_btn_widget.setProperty("class", "header__search__expand-button header__search__btn")
        self.expand_btn_widget.setObjectName("header__search__expand-button")
        expand_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "arrow-down-1.svg")))
        self.expand_btn_widget.setIcon(expand_icon)
        self.expand_btn_widget.clicked.connect(self.on_expand_btn_clicked)
        self.expand_status = False
        self.refresh_btn_widget = QPushButton(self)
        self.refresh_btn_widget.setProperty("class", "header__search__refresh-button header__search__btn")
        self.refresh_btn_widget.setObjectName("header__search__refresh-button")
        self.refresh_btn_widget.clicked.connect(self.on_refresh_btn_clicked)
        refresh_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "refresh.svg")))
        self.refresh_btn_widget.setIcon(refresh_icon)
        self.upload_btn_widget = QPushButton(self)
        self.upload_btn_widget.setProperty("class", "header__search__upload-button header__search__btn")
        self.upload_btn_widget.setObjectName("header__search__upload-button")
        self.upload_btn_widget.clicked.connect(self.on_upload_btn_clicked)
        upload_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "upload.svg")))
        self.upload_btn_widget.setIcon(upload_icon)
        self.download_btn_widget = QPushButton(self)
        self.download_btn_widget.setProperty("class", "header__search__download-button header__search__btn")
        self.download_btn_widget.setObjectName("header__search__download-button")
        self.download_btn_widget.clicked.connect(self.on_download_button_clicked)
        download_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "download.svg")))
        self.download_btn_widget.setIcon(download_icon)

        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        v_line.setFrameShadow(QFrame.Sunken)

        main_layout.addWidget(self.id_input_widget)
        main_layout.addWidget(self.expand_btn_widget)
        main_layout.addItem(QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addWidget(self.upload_btn_widget)
        main_layout.addWidget(self.download_btn_widget)
        main_layout.addWidget(v_line)
        main_layout.addWidget(self.refresh_btn_widget)

    def on_expand_btn_clicked(self):
        self.expand_status = not self.expand_status
        if not self.expand_status:
            icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "arrow-down-1.svg")))
        else:
            icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "arrow-up-1.svg")))
        self.expand_btn_widget.setIcon(icon)
    
    def on_refresh_btn_clicked(self): pass
    def on_upload_btn_clicked(self): pass
    def on_download_button_clicked(self): pass

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    sb = SearchBase()
    sb.show()

    sys.exit(app.exec_())
