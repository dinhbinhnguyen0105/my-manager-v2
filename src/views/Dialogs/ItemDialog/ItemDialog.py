import os, sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt, pyqtSignal

from Options.Options import Options
from Image.Image import Image
from Details.Details import Details
from Action.Action import Action

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.Components.Radio import Radio
from views.utils.widget_handler import WidgetHandler

class ItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "dialog")
        self.setObjectName("dialog")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)
        self.setFixedWidth(400)

        self.options_widget = Options(self)
        self.options_widget.event_current_value.connect(self.on_option_changed)
        self.image_widget = Image(self)
        # self.image_widget.setFixedSize(400, 200)
        self.details_widget = Details(self)
        self.action_widget = Action(self)
        self.action_widget.save_btn_widget.clicked.connect(self.on_save_btn_clicked)

        main_layout.addWidget(self.options_widget)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.image_widget)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.details_widget)
        h_line = QFrame()
        h_line.setFrameShape(QFrame.HLine)
        h_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(h_line)
        main_layout.addWidget(self.action_widget)

        with open(os.path.join(MY_DIR, "ItemDialog.styles.qss"), "r") as f:
            self.my_styles = f.read()
        self.setStyleSheet(self.my_styles)    
    
    def on_option_changed(self, payload):
        details_widgets = WidgetHandler.find_widgets_by_class(self.details_widget, QFrame, "item__details")
        for details_widget in details_widgets:
            if details_widget.property("user-data") == payload.get("options"):
                details_widget.show()
            else: details_widget.hide()

    def on_save_btn_clicked(self, ):
        option = self.options_widget.get_value()
        images = self.image_widget.get_value()
        details = self.details_widget.get_value()
        data = {
            **option,
            **details,
            **images,
        }
        print(data)
    
    def set_value(self, payload):
        self.options_widget.set_value(payload.get("options"))
        self.image_widget.set_value(payload.get("image"))
        details_widgets = WidgetHandler.find_widgets_by_class(self.details_widget, QFrame, "item__details")
        for details_widget in details_widgets:
            if details_widget.isHidden(): continue
            details_widget.set_value(payload.get("details"))

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    re = ItemDialog()
    re.show()
    sys.exit(app.exec_())

