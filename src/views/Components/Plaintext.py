from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QPlainTextEdit

class Plaintext(QFrame):
    e_text = pyqtSignal(str)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): self._class = payload["class"]
        else: self._class = None
        if "label" in payload.keys(): self._label = payload["label"]
        else: self._label = "undefined"
        
        self.setProperty("class", self._class)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        label_widget = QLabel(self._label, self)
        label_widget.setProperty("class", "label")
        self.plaintext_widget = QPlainTextEdit(self)
        self.plaintext_widget.setProperty("class", "plaintext")
        
        main_layout.addWidget(label_widget)
        main_layout.addWidget(self.plaintext_widget)
    
    def set_value(self, text):
        return self.plaintext_widget.setPlainText(text)

    def get_value(self):
        return self.plaintext_widget.toPlainText()