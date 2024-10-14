import os
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, os.path.pardir, os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))

class Footer(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "store__detail__footer")
        self.setObjectName("store__detail__footer")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.default_btn_widget = QPushButton(self)
        self.default_btn_widget.setObjectName("detail__footer__default-btn")
        self.default_btn_widget.setProperty("class", "detail__footer__btn detail__footer__default-btn")
        self.default_btn_widget.setProperty("user-data", "defaul-template")
        self.default_btn_widget.setText("Default")
        self.default_btn_widget.clicked.connect(self.on_default_btn_clicked)

        self.random_btn_widget = QPushButton(self)
        self.random_btn_widget.setObjectName("detail__footer__random-btn")
        self.random_btn_widget.setProperty("class", "detail__footer__btn detail__footer__random-btn")
        self.random_btn_widget.setProperty("user-data", "defaul-template")
        self.random_btn_widget.setText("Random")
        self.random_btn_widget.clicked.connect(self.on_random_btn_clicked)

        main_layout.addWidget(self.default_btn_widget)
        main_layout.addWidget(self.random_btn_widget)
    
    def on_default_btn_clicked(self): pass
    def on_random_btn_clicked(self): pass