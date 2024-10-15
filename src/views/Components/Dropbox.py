import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent

class Dropbox(QLabel):
    event_dropped_urls = pyqtSignal(list)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setProperty("class", "dropbox")
        self.setObjectName('dropbox')
        self.setText("Drag and drop images here")
    
    def dragEnterEvent(self, a0: QDragEnterEvent) -> None:
        if a0.mimeData().hasUrls():
            a0.accept()
        else:
            a0.ignore()

    def dragMoveEvent(self, a0: QDragMoveEvent) -> None:
        if a0.mimeData().hasUrls():
            a0.setDropAction(Qt.DropAction.CopyAction)
            a0.accept
        else:
            a0.ignore()

    def dropEvent(self, a0: QDropEvent) -> None:
        urls = []
        if a0.mimeData().hasUrls():
            a0.setDropAction(Qt.DropAction.CopyAction)
            a0.accept()
            for url in a0.mimeData().urls():
                if url.isLocalFile():
                    urls.append(str(url.toLocalFile()))
        else:
            a0.ignore()
        self.event_dropped_urls.emit(urls)