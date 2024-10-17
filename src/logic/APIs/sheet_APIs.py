import requests

SHEET_MACRO_URL = "https://script.google.com/macros/s/AKfycbz1G02TnGABEsI1LRFZmYHG51M-_k4OvJogt8HiIDuH_Ad9ZAdmNZWa6g9868UleQIq/exec"

class SheetAPI:
    def __init__(self):
        self.method = ""
        self.sheet_name = ""
        self.data = {}

    def get_sheets(self):
        try:
            response = requests.get(SHEET_MACRO_URL)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            raise err

    def get(self, payload):
        self.method = "get"
        self.sheet_name = payload['sheetName']
        self.data = {}
        try:
            response = requests.post(SHEET_MACRO_URL, json={"method": self.method, "sheetName": self.sheet_name, "data": self.data})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            raise err

    def post(self, payload):
        self.method = "post"
        self.sheet_name = payload['sheetName']
        self.data = payload['data']
        try:
            response = requests.post(SHEET_MACRO_URL, json={"method": self.method, "sheetName": self.sheet_name, "data": self.data})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            raise err

    def delete(self, payload):
        self.method = "delete"
        self.sheet_name = payload['sheetName']
        self.data = payload['data']
        try:
            response = requests.post(SHEET_MACRO_URL, json={"method": self.method, "sheetName": self.sheet_name, "data": self.data})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            raise err

    def put(self, payload):
        self.method = "put"
        self.sheet_name = payload['sheetName']
        self.data = payload['data']
        try:
            response = requests.post(SHEET_MACRO_URL, json={"method": self.method, "sheetName": self.sheet_name, "data": self.data})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            raise err

sheet_api = SheetAPI()
a = sheet_api.get({
    "sheetName": "real-estate"
})

for data in a.get("retrievedData"):
    print(data)
    exit()

{'id': 'R919.89599',
'type': 'rent',
'date': '2024-09-07T17:00:00.000Z',
'status': 'available',
'flag': 2, 'category': 'house',
'province': 'lamdong',
'district': 'dalat',
'ward': 10, 'street': 'Phạm Hồng Thái',
'area': '',
'construction': '1 trệt',
'function': '1pk, 1 bếp, 2pn, 1wc',
'buildingline': 'undefined',
'furniture': 'basic',
'legal': 'undefined',
'price': '10,5',
'description': '+ Đường xe hơi 9m rộng rãi\n+ Tổng diện tích 150m2; sân trước nhà rộng rãi\n+ Có gara để xe hơi, chỗ để xe máy, sân phơi đồ.\n+ Có bình nước nóng lạnh + dàn năng lượng mặt trời.',
'images': '[{"name":"20240907151137_0.png","id":"1wTDXYDs8ygPXHNN_a7FMrnbkbFDlCkif"},{"name":"20240907151137_1.png","id":"10Cn3Jzah6--xHi52nTQiol8VvsARdaTQ"},{"name":"20240907151137_2.png","id":"169FRot3W0QFiUeUrqW2dpHBigi52Khzy"},{"name":"20240907151137_3.png","id":"1z_DoXrFE74hvPvlFA4MtvvWargUw5MEB"},{"name":"20240907151137_4.png","id":"1mtOL5ablJd8wp1eRbCoUDy5scM6F2sGE"},{"name":"20240907151137_5.png","id":"1JnDJIRi0TKqy8v4OwQliysMw3XLE0KW8"},{"name":"20240907151137_6.png","id":"1QYzvFt70pbbXqipldoStmra1iMU67R7L"},{"name":"20240907151137_7.png","id":"13JIK80KWbdnHwIFfX_j6yQ38DeHTedGW"},{"name":"20240907151137_8.png","id":"1QMYqXqbEnCE5c7VZ8k-O8fm9gLgWN7j-"},{"name":"20240907151137_9.png","id":"1VGcWEoxa5a6qUqkCffRNcKEVWsAduh1-"}]'
}