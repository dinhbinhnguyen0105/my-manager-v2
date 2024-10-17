import os, sys
from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from .List.List import List
from .Detail.Detail import Detail

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir, ))
ASSETS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "assets"))
sys.path.append(SRC_DIR)
from views.Dialogs.ItemDialog.ItemDialog import ItemDialog
from views.utils.widget_handler import WidgetHandler
from logic.utils.temp_handle import TemplateHandler
from logic.utils.product_handler import ProductHandler

class Store(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "page__store page")
        self.setProperty("user-data", "store")
        self.setObjectName("page__store")
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        main_layout.setAlignment(Qt.AlignTop)

        self.id_product = None

        self.list_widget = List(self)
        self.set_current_item()
        self.detail_widget = Detail(self)
        self.detail_widget.setFixedWidth(300)
        self.detail_widget.header_widget.set_disable(True)
        self.detail_widget.footer_widget.set_disable(True)

        self.detail_widget.header_widget.add_btn_widget.clicked.connect(self.on_add_clicked)
        self.detail_widget.header_widget.edit_btn_widget.clicked.connect(self.on_edit_clicked)
        self.detail_widget.header_widget.status_btn_widget.clicked.connect(self.on_status_clicked)
        self.detail_widget.header_widget.delete_btn_widget.clicked.connect(self.on_delete_clicked)
        

        main_layout.addWidget(self.list_widget)
        v_line = QFrame()
        v_line.setFrameShape(QFrame.VLine)
        v_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(v_line)
        main_layout.addWidget(self.detail_widget)
    
    def set_current_item(self):
        table = WidgetHandler.find_widget_by_id(self, QFrame, "store__list__table")
        table.table_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselecated):
        self.detail_widget.header_widget.set_disable(False)
        self.detail_widget.footer_widget.set_disable(False)
        for index in selected.indexes():
            if index.data(Qt.UserRole).lower() == "id":
                options_widget = WidgetHandler.find_widget_by_id(self, QFrame, "list__header__options")
                product_info = ProductHandler.get_product_buy_id({ **options_widget.get_value(), "id": index.data().lower()})
                product = TemplateHandler.render_content({ "action": "default", "product_info": product_info})
                if "images" not in product_info.keys(): imgs_of_product_path = []
                else: imgs_of_product_path = ProductHandler.get_images_buy_path(product_info["images"])
                if "status" not in product_info.keys(): status = "available"
                else: status = product_info["status"]
                
                self.detail_widget.body_widget.set_value({
                    "images": imgs_of_product_path,
                    "title": product.get("title"),
                    "description": product.get("description")
                })
                self.id_product = index.data().lower()
                if len(imgs_of_product_path):
                    self.detail_widget.body_widget.images_widget.show()
                else: self.detail_widget.body_widget.images_widget.hide()
                if status == "available":
                    block_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "block.svg")))
                    self.detail_widget.header_widget.status_btn_widget.setProperty("class", "detail__header__btn detail__header__status-btn detail__header__status-btn--block")
                    self.detail_widget.header_widget.status_btn_widget.setProperty("user-data", "block")
                    self.detail_widget.header_widget.status_btn_widget.setIcon(block_icon)
                elif status == "unavailable":
                    self.detail_widget.header_widget.status_btn_widget.setProperty("class", "detail__header__btn detail__header__status-btn detail__header__status-btn--check")
                    check_icon = QIcon(os.path.abspath(os.path.join(ASSETS_DIR, "icons", "check.svg")))
                    self.detail_widget.header_widget.status_btn_widget.setIcon(check_icon)
                self.setStyleSheet(self.styleSheet())

    def on_add_clicked(self):
        self.item_dialog = ItemDialog(self)
        self.item_dialog.show()

    def on_edit_clicked(self):
        # self.id_product
        pass
    def on_status_clicked(self):
        pass
    def on_delete_clicked(self): pass

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    store = Store()
    store.show()

    sys.exit(app.exec_())

# /Users/dinhbinh/Dev/my-manager/my-manager-v2/bin/db/products/real-estate/real-estate.json