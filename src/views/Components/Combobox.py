from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QComboBox, QLabel


class Combobox(QFrame):
    e_option = pyqtSignal(tuple)
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): self._class = payload["class"]
        else: self._class = None
        if "label" in payload.keys(): self._label = payload["label"]
        else: self._label = "undefined"
        if "options" in payload.keys(): self._options = payload["options"]
        else: self._options = []

        self.setProperty("class", self._class)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)

        label_widget = QLabel(self._label, self)
        label_widget.setProperty("class", "label")
        self.combobox_widget = QComboBox(self)
        self.combobox_widget.setProperty("class", "combobox")
        for index, _option in enumerate(self._options):
            self.combobox_widget.addItem(_option[0])
            self.combobox_widget.setItemData(index, _option[1], Qt.UserRole)
        self.combobox_widget.currentIndexChanged.connect(self.on_index_changed)
        
        main_layout.addWidget(label_widget)
        main_layout.addWidget(self.combobox_widget)
    
    def showEvent(self, e):
        self.e_option.emit((
            self.combobox_widget.currentText(),
            self.combobox_widget.currentData()
        ))
    
    def on_index_changed(self, index):
        self.e_option.emit((
            self.combobox_widget.currentText(),
            self.combobox_widget.currentData()
        ))
    
    def set_option(self, payload):
        self.combobox_widget.clear()
        self._options = payload
        for index, _option in enumerate(payload):
            self.combobox_widget.addItem(_option[0])
            self.combobox_widget.setItemData(index, _option[1], Qt.UserRole)
    
    def set_value(self, option_text):
        for i in range(self.combobox_widget.count()):
            item = self.combobox_widget.itemText(i)
            if item.lower() == option_text.lower():
                self.combobox_widget.setCurrentIndex(i)
                return True
    
    def get_value(self):
        return (
            self.combobox_widget.currentText(),
            self.combobox_widget.currentData()
        )

# if __name__ == "__main__":
#     from PyQt5.QtWidgets import QApplication
#     import sys

#     app = QApplication(sys.argv)
#     window = Combobox({ "options": [
#         ("House", "category_house"),
#         ("Shophouse", "category_shophouse"),
#         ("Villa", "category_villa"),
#         ("Apartment", "category_apartment"),
#         ("Homestay", "category_homestay"),
#         ("Hotel", "category_hotel"),
#         ("Land", "category_land"),
#     ]})
#     window.show()
#     window.set_value("Homestay")
#     print(window.get_value())
#     sys.exit(app.exec_())