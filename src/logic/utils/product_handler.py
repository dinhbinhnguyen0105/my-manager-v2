import os, sys, json, shutil

MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, ))
DB_PRODUCTS_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "bin", "db", "products"))

sys.path.append(SRC_DIR)
from logic.utils.file_handler import FileHandler

class ProductHandler():
    def read(name):
        data_path = FileHandler.get_path_of_file_data(name)
        with open(data_path, "r", encoding="utf8") as f:
            data = json.load(f)
            results = []
            for value in data.values():
                results += value
        return results
    def get_product_buy_id(payload):
        if "option" not in payload.keys(): raise CustomError("option not in payload.keys()")
        if "id" not in payload.keys(): raise CustomError("id not in payload.keys()")
        product_path = os.path.abspath(os.path.join(DB_PRODUCTS_DIR, payload["option"], f"{payload['option']}.json"))
        if not os.path.exists(product_path): raise CustomError("product path not exists")
        with open(product_path, "r", encoding="utf8") as f:
            data = json.load(f)
            if payload["option"] == "real-estate":
                for products in data.values():
                    for product in products:
                        if "id" in product.keys() and product["id"].lower() == payload["id"].lower(): return product
            elif payload["option"] == "miscellaneous":
                for id in data.keys():
                    if id.lower() == payload["id"].lower(): return data[id]
        raise CustomError("id not in data")
    @staticmethod
    def get_images_buy_path(_path):
        if not os.path.exists(_path): raise CustomError("images path not exists")
        imgs_in_dir = []
        list_file = os.listdir(_path)
        list_file.sort()
        for index, file in enumerate(list_file):
            if index > 6: break
            if file.split(".")[-1] in ["jpg", "png", "jpeg"]: imgs_in_dir.append(os.path.abspath(os.path.join(_path, file)))
        return imgs_in_dir

class CustomError(Exception):
    pass

if __name__ == "__main__":
    ProductHandler.read("real-estate")