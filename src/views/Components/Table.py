from PyQt5.QtCore import pyqtSignal, QSortFilterProxyModel, Qt
from PyQt5.QtWidgets import QFrame,  QVBoxLayout, QLabel, QTableView, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Table(QFrame):
    def __init__(self, payload, parent=None):
        super().__init__(parent)
        if "class" in payload.keys(): _class = payload["class"]
        else: _class = False
        if "label" in payload.keys(): _label = payload["label"]
        else: _label = False

        if _class: self.setProperty("class", _class)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        if _label:
            label_widget = QLabel(_label, self)
            label_widget.setProperty("class", "label")
            main_layout.addWidget(label_widget)

        self.model = QStandardItemModel()

        self.set_model({
            "headers": [
                ("date", "Date"),
                ("id", "ID"),
                ("type", "Type"),
                ("ward", "Ward"),
                ("street", "Street"),
                ("category", "Category"),
                ("area", "Area"),
                ("price", "Price"),
                ("building_line", "Building line"),
                ("function", "Function"),
                ("furniture", "Furniture"),
                ("legal", "Legal"),
            ],
            "data": [
                {
                    "option": "real-estate",
                    "date": "10-12-24",
                    "images": "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.r.101224.481",
                    "id": "re.r.101224.481",
                    "provide": "lamdong",
                    "district": "dalat",
                "ward": "ward_3",
                    "street": "tr\u1ea7n ph\u00fa",
                    "type": "rent",
                    "category": "category_homestay",
                    "building_line": "motorbike",
                    "area": 0.0,
                    "construction": "1 tr\u1ec7t, 1 l\u1ea7u",
                    "function": "1pk, 1 b\u1ebfp, 1pn, 1wc",
                    "furniture": "full",
                    "legal": False,
                    "price": 12.0,
                    "description": "- cho thu\u00ea homestay g\u1ed7 , s\u00e2n v\u01b0\u1eddn bbq ngay trung t\u00e2m \u0111\u00e0 l\u1ea1t \n- nh\u00e0 n\u1ed9i th\u1ea5t g\u1ed7 \u1ea5m c\u00fang nh\u01b0 trong h\u00ecn"
                },
            ]
        })
        
        self.proxy_model = MultiColumnFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        
        # Tạo QTableView để hiển thị bảng
        self.table_view = QTableView()
        self.table_view.setModel(self.proxy_model)

        btn = QPushButton("Click me", self,)
        btn.clicked.connect(self.on_click)

        main_layout.addWidget(self.table_view)
        main_layout.addWidget(btn)


    def set_model(self, payload):
        if "headers" not in payload.keys(): pass
        if "data" not in payload.keys(): pass
        self.model.clear()
        self.model.setHorizontalHeaderLabels([headers[1] for headers in payload.get("headers")])
        for row in payload.get("data"):
            items = []
            header_user_data = [headers[0] for headers in payload.get("headers")]
            while len(header_user_data):
                user_data = header_user_data.pop(0)
                for key in row.keys():
                    if user_data == key:
                        items.append(QStandardItem(str(row.get(key))))
                        continue
            self.model.appendRow(items)
        self.model.layoutChanged.emit()
        

    def on_click(self):
        self.set_model({
            "headers": [
                ("date", "Date"),
                ("id", "ID"),
                ("type", "Type"),
                ("ward", "Ward"),
                ("street", "Street"),
                ("category", "Category"),
                ("area", "Area"),
                ("price", "Price"),
                ("building_line", "Building line"),
                ("function", "Function"),
                ("furniture", "Furniture"),
                ("legal", "Legal"),
            ],
            "data": [
                {
                    "option": "real-estate",
                    "date": "10-12-24",
                    "images": "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.r.101224.481",
                    "id": "re.r.101224.481",
                    "provide": "lamdong",
                    "district": "dalat",
                "ward": "ward_3",
                    "street": "tr\u1ea7n ph\u00fa",
                    "type": "rent",
                    "category": "category_homestay",
                    "building_line": "motorbike",
                    "area": 0.0,
                    "construction": "1 tr\u1ec7t, 1 l\u1ea7u",
                    "function": "1pk, 1 b\u1ebfp, 1pn, 1wc",
                    "furniture": "full",
                    "legal": False,
                    "price": 12.0,
                    "description": "- cho thu\u00ea homestay g\u1ed7 , s\u00e2n v\u01b0\u1eddn bbq ngay trung t\u00e2m \u0111\u00e0 l\u1ea1t \n- nh\u00e0 n\u1ed9i th\u1ea5t g\u1ed7 \u1ea5m c\u00fang nh\u01b0 trong h\u00ecn"
                },
                {
                    "option": "real-estate",
                    "date": "10-12-24",
                    "images": "/Users/dinhbinh/Dev/my-manager/my-manager/bin/db/real-estate/images/re.r.101224.481",
                    "id": "re.r.101224.481",
                    "provide": "lamdong",
                    "district": "dalat",
                "ward": "ward_3",
                    "street": "tr\u1ea7n ph\u00fa",
                    "type": "rent",
                    "category": "category_homestay",
                    "building_line": "motorbike",
                    "area": 0.0,
                    "construction": "1 tr\u1ec7t, 1 l\u1ea7u",
                    "function": "1pk, 1 b\u1ebfp, 1pn, 1wc",
                    "furniture": "full",
                    "legal": False,
                    "price": 12.0,
                    "description": "- cho thu\u00ea homestay g\u1ed7 , s\u00e2n v\u01b0\u1eddn bbq ngay trung t\u00e2m \u0111\u00e0 l\u1ea1t \n- nh\u00e0 n\u1ed9i th\u1ea5t g\u1ed7 \u1ea5m c\u00fang nh\u01b0 trong h\u00ecn"
                },
            ]
        })
        pass


class MultiColumnFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.column_filters = {}

    # Thêm bộ lọc cho mỗi cột
    def setFilterForColumn(self, column, pattern):
        if pattern:
            self.column_filters[column] = pattern
        else:
            if column in self.column_filters:
                del self.column_filters[column]
        self.invalidateFilter()

    # Ghi đè phương thức để kiểm tra từng hàng
    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()
        
        # Duyệt qua tất cả các cột và kiểm tra điều kiện bộ lọc
        for column, pattern in self.column_filters.items():
            index = model.index(source_row, column, source_parent)
            data = model.data(index)
            if pattern.lower() not in str(data).lower():
                return False  # Nếu dữ liệu không khớp với mẫu ở bất kỳ cột nào, ẩn hàng này

        return True  # Nếu dữ liệu khớp với tất cả các bộ lọc, hiển thị hàng


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)

    window = Table({})
    window.show()

    sys.exit(app.exec_())