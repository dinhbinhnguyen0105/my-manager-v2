import sys
from PyQt5.QtWidgets import QApplication, QTableView, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QSortFilterProxyModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem


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


class TableWithMultiColumnFilter(QWidget):
    def __init__(self):
        super().__init__()

        # Tạo QStandardItemModel để chứa dữ liệu bảng
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'Name', 'Age'])

        # Thêm một số dữ liệu mẫu vào model
        data = [
            ['1', 'John', '25'],
            ['2', 'Anna', '30'],
            ['3', 'Mike', '22'],
            ['4', 'Sara', '27'],
            ['5', 'John', '24']
        ]
        
        for row in data:
            items = [QStandardItem(field) for field in row]
            self.model.appendRow(items)

        # Tạo MultiColumnFilterProxyModel để áp dụng bộ lọc trên nhiều cột
        self.proxy_model = MultiColumnFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        # Tạo QTableView để hiển thị bảng
        self.table_view = QTableView()
        self.table_view.setModel(self.proxy_model)

        # Tạo QLineEdit để nhập văn bản cần lọc trên cột 'Name'
        self.name_filter_edit = QLineEdit()
        self.name_filter_edit.setPlaceholderText("Lọc theo tên...")
        self.name_filter_edit.textChanged.connect(self.filter_table)

        # Tạo QLineEdit để nhập văn bản cần lọc trên cột 'Age'
        self.age_filter_edit = QLineEdit()
        self.age_filter_edit.setPlaceholderText("Lọc theo tuổi...")
        self.age_filter_edit.textChanged.connect(self.filter_table)

        # Layout để sắp xếp các widget
        layout = QVBoxLayout()
        layout.addWidget(self.name_filter_edit)
        layout.addWidget(self.age_filter_edit)
        layout.addWidget(self.table_view)
        self.setLayout(layout)

    # Hàm áp dụng bộ lọc cho bảng
    def filter_table(self):
        # Lấy văn bản từ các ô nhập để lọc theo cột 'Name' và 'Age'
        name_filter = self.name_filter_edit.text()
        age_filter = self.age_filter_edit.text()

        # Thiết lập bộ lọc cho từng cột
        self.proxy_model.setFilterForColumn(1, name_filter)  # Cột 1 là "Name"
        self.proxy_model.setFilterForColumn(2, age_filter)   # Cột 2 là "Age"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWithMultiColumnFilter()
    window.setWindowTitle('Table with Multi-Column Filter')
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())
