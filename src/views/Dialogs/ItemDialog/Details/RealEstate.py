import os, sys, datetime, random
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir,os.path.pardir,os.path.pardir,os.path.pardir,))
sys.path.append(SRC_DIR)
from views.Components.Radio import Radio
from views.Components.Combobox import Combobox
from views.Components.Plaintext import Plaintext
from views.Components.Lineedit import Lineedit
from views.utils.widget_handler import WidgetHandler

class RealEstate(QFrame):
    event_current_value = pyqtSignal(dict)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setProperty("class", "real-estate dialog__details")
        self.setProperty("user-data", "real-estate")
        self.setObjectName("real-estate")
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        location_layout = QGridLayout()
        location_layout.setContentsMargins(0,0,0,0)
        location_layout.setSpacing(0)
        location_layout.setAlignment(Qt.AlignTop)
        details_layout = QGridLayout()
        details_layout.setContentsMargins(0,0,0,0)
        details_layout.setSpacing(0)
        details_layout.setAlignment(Qt.AlignTop)
        basic_layout = QHBoxLayout()
        basic_layout.setContentsMargins(0,0,0,0)
        basic_layout.setSpacing(0)
        basic_layout.setAlignment(Qt.AlignCenter)

        self.type_widget = Radio({
            "class": "type__input real-estate__item",
            "id" : "type__input",
            "user-data" : "type",
            # "label": "type: ".title()
        }, self)
        self.type_widget.event_current_value.connect(self.on_type_changed)
        self.buildingline_widget = Radio({
            "class": "buildingline__input real-estate__item",
            "id" : "buildingline__input",
            "user-data" : "buildingline",
            # "label": "buildingline: ".title()
        }, self)
        self.categories_widget = Combobox({
            "class": "categories__input real-estate__item",
            "id" : "categories__input",
            "user-data" : "categories",
            "label": "categories: ".title()
        }, self)
        self.categories_widget.event_current_value.connect(self.on_categories_changed)
        self.description_widget = Plaintext({
            "class": "description__input real-estate__item",
            "id" : "description__input",
            "user-data" : "description",
            "label": "description: ".title()
        }, self)
        self.location_provide_widge = Combobox({
            "class": "provide__input real-estate__item",
            "id" : "provide__input",
            "user-data" : "provide",
            "label": "provide: ".title()
        }, self)
        self.location_district_widge = Combobox({
            "class": "district__input real-estate__item",
            "id" : "district__input",
            "user-data" : "district",
            "label": "district: ".title()
        }, self)
        self.location_ward_widge = Combobox({
            "class": "ward__input real-estate__item",
            "id" : "ward__input",
            "user-data" : "ward",
            "label": "ward: ".title()
        }, self)
        self.location_street_widge = Lineedit({
            "class": "street__input real-estate__item",
            "id" : "street__input",
            "user-data" : "street",
            "label": "street: ".title()
        }, self)
        self.details_area_widget = Lineedit({
            "class": "area__input real-estate__item",
            "id" : "area__input",
            "user-data" : "area",
            "label": "area: ".title()
        }, self)
        self.details_construction_widget = Lineedit({
            "class": "construction__input real-estate__item",
            "id" : "construction__input",
            "user-data" : "construction",
            "label": "construction: ".title()
        }, self)
        self.details_function_widget = Lineedit({
            "class": "function__input real-estate__item",
            "id" : "function__input",
            "user-data" : "function",
            "label": "function: ".title()
        }, self)
        self.details_furniture_widget = Combobox({
            "class": "furniture__input real-estate__item",
            "id" : "furniture__input",
            "user-data" : "furniture",
            "label": "furniture: ".title()
        }, self)
        self.details_legal_widget = Combobox({
            "class": "legal__input real-estate__item",
            "id" : "legal__input",
            "user-data" : "legal",
            "label": "legal: ".title()
        }, self)
        self.details_price_widget = Lineedit({
            "class": "price__input real-estate__item",
            "id" : "price__input",
            "user-data" : "price",
            "label": "price: ".title()
        }, self)
        self.id_widget = QLabel(self)
        self.id_widget.setProperty("class", "id__label")
        self.id_widget.setProperty("user-data", "id")
        self.id_widget.setObjectName("id__label")
        self.date_widget = QLabel(self)
        self.date_widget.setProperty("class", "date__label")
        self.date_widget.setProperty("user-data", "date")
        self.date_widget.setObjectName("date__label")
        self.set_date()
        basic_layout.addWidget(self.date_widget)
        basic_layout.addWidget(self.id_widget)
        location_layout.addWidget(self.location_provide_widge, 0, 0, 1, 1)
        location_layout.addWidget(self.location_district_widge, 0, 1, 1, 2)
        location_layout.addWidget(self.location_ward_widge, 1, 0, 1, 1)
        location_layout.addWidget(self.location_street_widge, 1, 1, 1, 2)
        details_layout.addWidget(self.details_area_widget, 0, 0, 1, 1)
        details_layout.addWidget(self.details_construction_widget, 0, 1, 1, 1)
        details_layout.addWidget(self.details_function_widget, 1, 0, 1, 1)
        details_layout.addWidget(self.details_furniture_widget, 1, 1, 1, 1)
        details_layout.addWidget(self.details_legal_widget, 2, 0, 1, 1)
        details_layout.addWidget(self.details_price_widget, 2, 1, 1, 1)

        main_layout.addLayout(basic_layout)
        main_layout.addWidget(self.type_widget)
        main_layout.addWidget(self.categories_widget)
        main_layout.addLayout(location_layout)
        main_layout.addWidget(self.buildingline_widget)
        main_layout.addLayout(details_layout)
        main_layout.addWidget(self.description_widget)

        self.set_options()
        self.get_value()
    
    def showEvent(self, e):
        self.set_value([
            { "type" : "sell" },
            { "ward" : "1"},
            { "buildingline": "motorbike"}
        ])

    def set_value(self, payload):
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "real-estate__item")
        for obj in payload:
            for index, input_widget in enumerate(input_widgets):
                for key in obj.keys():
                    if input_widget.property("user-data") == key:

                        input_widget.set_value(obj)
                        input_widgets.pop(index)
    
    def get_value(self):
        data = {}
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "real-estate__item")
        for input_widget in input_widgets:
            data = {
                **data,
                **input_widget.get_value()
            }
        return {
            **data,
            **{ "id" : self.id_widget.text()},
            **{ "date" : self.date_widget.text()},
            **{ "status": "available"},
        }
    
    def set_options(self):
        input_widgets = WidgetHandler.find_widgets_by_class(self, QFrame, "real-estate__item")
        for input_widget in input_widgets:
            if input_widget.property("user-data") == "type":
                input_widget.set_options([
                    {
                        "id": "item__type__sell",
                        "class": "item__type__sell",
                        "user-data": "sell",
                        "label": "sell".capitalize(),
                    },
                    {
                        "id": "item__type__rent",
                        "class": "item__type__rent",
                        "user-data": "rent",
                        "label": "rent".capitalize(),
                    },
                    {
                        "id": "item__type__assignment",
                        "class": "item__type__assignment",
                        "user-data": "assignment",
                        "label": "assignment".capitalize(),
                    },
                ])
            elif input_widget.property("user-data") == "buildingline": 
                input_widget.set_options([
                    {
                        "id": "item__buildingline__motorbike",
                        "class": "item__buildingline__motorbike",
                        "user-data": "motorbike",
                        "label": "motorbike".capitalize(),
                    },
                    {
                        "id": "item__buildingline__car",
                        "class": "item__buildingline__car",
                        "user-data": "car",
                        "label": "car".capitalize(),
                    },
                ])
            elif input_widget.property("user-data") == "categories":
                input_widget.set_options([
                    {"user-data": "house", "label": "House", },
                    {"user-data": "shophouse", "label": "Shophouse", },
                    {"user-data": "villa", "label": "Villa", },
                    {"user-data": "apartment", "label": "Apartment", },
                    {"user-data": "homestay", "label": "Homestay", },
                    {"user-data": "hotel", "label": "Hotel", },
                    {"user-data": "land", "label": "Land", },
                    {"user-data": "retailspace", "label": "Retail space", },
                    {"user-data": "workshop", "label": "Workshop", },
                    {"user-data": "coffeehouse", "label": "Coffee house", },
                ])
            elif input_widget.property("user-data") == "provide":
                input_widget.set_options([
                    {"user-data": "lamdong", "label": "Lâm Đồng", },
                ])
            elif input_widget.property("user-data") == "district":
                input_widget.set_options([
                    {"user-data": "dalat", "label": "Đà Lạt", },
                ])
            elif input_widget.property("user-data") == "ward":
                input_widget.set_options([
                    { "label" : "Ward 1", "user-data" : "1" },
                    { "label" : "Ward 2", "user-data" : "2" },
                    { "label" : "Ward 3", "user-data" : "3" },
                    { "label" : "Ward 4", "user-data" : "4" },
                    { "label" : "Ward 5", "user-data" : "5" },
                    { "label" : "Ward 6", "user-data" : "6" },
                    { "label" : "Ward 7", "user-data" : "7" },
                    { "label" : "Ward 8", "user-data" : "8" },
                    { "label" : "Ward 9", "user-data" : "9" },
                    { "label" : "Ward 10", "user-data" : "10" },
                    { "label" : "Ward 11", "user-data" : "11" },
                    { "label" : "Ward 12", "user-data" : "12" },
                    { "label" : "Ward Tà Nung", "user-data" : "tanung" },
                    { "label" : "Ward Trạm Hành", "user-data" : "tramhanh" },
                    { "label" : "Ward Xuân Trường", "user-data" : "xuantruong" },
                    { "label" : "Ward Xuân Thọ", "user-data" : "xuantho" },
                ])
            elif input_widget.property("user-data") == "furniture":
                input_widget.set_options([
                    {"label": "None", "user-data" : "none"},
                    {"label": "Basic", "user-data" : "basic"},
                    {"label": "Full", "user-data" : "full"},
                ])
            elif input_widget.property("user-data") == "legal":
                input_widget.set_options([
                    {"label": "Không sổ", "user-data": "none"},
                    {"label": "Sổ nông nghiệp chung", "user-data": "snnc"},
                    {"label": "Sổ nông nghiệp phân quyền", "user-data": "snnpq"},
                    {"label": "Sổ nông nghiệp riêng", "user-data": "srnn"},
                    {"label": "Sổ xây dựng chung", "user-data": "sxdc"},
                    {"label": "Sổ xây dựng phân quyền", "user-data": "sxdpq"},
                    {"label": "Sổ xây dựng riêng", "user-data": "srxd"},
                ])

    def on_type_changed(self, _type):
        if _type.get("type") == "sell":
            self.set_id("S")
            self.set_categories(_type)
            self.details_area_widget.setDisabled(False)
            self.details_legal_widget.setDisabled(False)
        elif _type.get("type") == "rent":
            self.set_id("R")
            self.set_categories(_type)
            self.details_area_widget.set_value({ "area" : ""})
            self.details_area_widget.setDisabled(True)
            self.details_legal_widget.setDisabled(True)
        elif _type.get("type") == "assignment":
            self.set_id("A")
            self.set_categories(_type)
            self.details_area_widget.set_value({ "area" : ""})
            self.details_area_widget.setDisabled(True)
            self.details_legal_widget.setDisabled(True)
    
    def on_categories_changed(self, category):
        category = category.get("categories")
        if category == "apartment" or\
            category == "retailspace" or\
            category == "workshop":
            self.details_construction_widget.set_value({ "construction" : "" })
            self.details_construction_widget.setEnabled(False)
            self.details_function_widget.setEnabled(True)
            self.details_furniture_widget.setEnabled(True)
        elif category == "land":
            self.details_construction_widget.set_value({ "construction" : "" })
            self.details_construction_widget.setEnabled(False)
            self.details_function_widget.set_value({ "function" : "" })
            self.details_function_widget.setEnabled(False)
            self.details_furniture_widget.setEnabled(False)
        else:
            self.details_construction_widget.set_value({ "construction" : "" })
            self.details_construction_widget.setEnabled(True)
            self.details_function_widget.setEnabled(True)
            self.details_furniture_widget.setEnabled(True)

    def set_id(self, _type):
        now = datetime.datetime.now()
        randint = random.randint(0, 100)
        id = f"{now.strftime('%m')}{now.strftime('%d')}{now.strftime('%y')}.{int(now.strftime('%S'))* randint}"
        self.id_widget.setText(f"RE.{_type}.{id}".upper())

    def set_date(self,):
        now = datetime.datetime.now()
        date = f"{now.strftime('%m')}-{now.strftime('%d')}-{now.strftime('%y')}"
        self.date_widget.setText(date)

    def set_categories(self, _type):
        if _type.get("type") == "sell":
            self.categories_widget.set_options([
                {"label": "House", "user-data": "house"},
                {"label": "Shophouse", "user-data": "shophouse"},
                {"label": "Villa", "user-data": "villa"},
                {"label": "Apartment", "user-data": "apartment"},
                {"label": "Homestay", "user-data": "homestay"},
                {"label": "Hotel", "user-data": "hotel"},
                {"label": "Land", "user-data": "land"},

            ])
        elif _type.get("type") == "rent": 
            self.categories_widget.set_options([
                {"label": "House", "user-data": "house"},
                {"label": "Shophouse", "user-data": "shophouse"},
                {"label": "Villa", "user-data": "villa"},
                {"label": "Apartment", "user-data": "apartment"},
                {"label": "Homestay", "user-data": "homestay"},
                {"label": "Hotel", "user-data": "hotel"},
                {"label": "Retail space", "user-data": "retailspace"},
                {"label": "Workshop", "user-data": "workshop"},
                {"label": "Coffee house", "user-data": "coffeehouse"},
            ])
        elif _type.get("type") == "assignment": 
            self.categories_widget.set_options([
                {"label": "Homestay", "user-data": "homestay"},
                {"label": "Hotel", "user-data": "hotel"},
                {"label": "Land", "user-data": "land"},
                {"label": "Retail space", "user-data": "retailspace"},
                {"label": "Workshop", "user-data": "workshop"},
                {"label": "Coffee house", "user-data": "coffeehouse"},
            ])






