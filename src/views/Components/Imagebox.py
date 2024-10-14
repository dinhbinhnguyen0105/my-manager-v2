import platform, os, subprocess, sys
from pathlib import Path
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMouseEvent, QCloseEvent, QWheelEvent

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.utils.widget_handler import WidgetHandler

class Imagebox(QFrame):
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): _class = payload["class"]
        else: _class = None
        if "label" in payload.keys(): label = payload["label"]
        else: label = False
        if "id" in payload.keys(): id = payload["id"]
        else: id = False
        if "user-data" in payload.keys(): user_data = payload["user-data"]
        else: user_data = False

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(main_layout)
        
        self.setProperty("class", _class)
        if id: self.setObjectName(id)
        if user_data: self.setProperty("user-data", payload["user-data"])
        self.prev_point, self.curr_point, self.slide, self.images_count, self.image_folder, self.urls = 0, 0, 0, 0, None, []
        WidgetHandler.add_class(self, "image-box")
        if label:
            self.label_widget = QLabel(label, self)
            self.label_widget.setProperty("class", "label")
            main_layout.addWidget(self.label_widget)
            main_layout.addWidget(self.label_widget)

        self.main_widget = QStackedWidget(self)
        self.main_widget.setContentsMargins(0,0,0,0)
        main_layout.addWidget(self.main_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        
    def set_value(self, urls):
        img_widgets = WidgetHandler.find_widgets_by_class(self, Image, "image")
        for img_widget in img_widgets:
            img_widget.setParent(None)
            img_widget.deleteLater()
        self.img_count = len(urls)
        self.urls = urls
        for url in self.urls:
            img = Image(url, self)
            self.main_widget.addWidget(img)
        self.main_widget.setCurrentIndex(0)
    
    def closeEvent(self, a0: QCloseEvent | None) -> None:
        return super().closeEvent(a0)
    
    def wheelEvent(self, a0: QWheelEvent) -> None:
        self.curr_point += a0.pixelDelta().y()
        if self.curr_point < self.prev_point:
            self.slide -= 1
        elif self.curr_point > self.prev_point:
            self.slide += 1
        self.prev_point = self.curr_point
        if self.slide < 1:
            self.slide = 1
        if self.slide > self.img_count:
            self.slide = self.img_count
        self.main_widget.setCurrentIndex(self.slide)

class Image(QLabel):
    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.url = url
        self.setProperty("class", "image")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pixmap = QPixmap(url)
        self.pixmap = self.pixmap.scaled(
            self.parent().size(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(self.pixmap)
    
    def set_value(self, url):
        self.pixmap = QPixmap(url)
        self.pixmap = self.pixmap.scaled(
            self.parent().size(),
            aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio,
            transformMode=Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(self.pixmap)

    def get_value(self):
        return self.url
    
    def mousePressEvent(self, ev: QMouseEvent | None) -> None:
        if self.url == None: return
        else:
            url = Path(self.url)
        if platform.system() == "Windows":
            os.startfile(url.parent)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", url.parent])
        else:
            subprocess.Popen(["xdg-open", url.parent])
