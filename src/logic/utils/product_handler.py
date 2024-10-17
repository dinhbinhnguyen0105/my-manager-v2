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
    @staticmethod
    def get_product_buy_id(payload):
        if "options" not in payload.keys(): raise CustomError("option not in payload.keys()")
        if "id" not in payload.keys(): raise CustomError("id not in payload.keys()")

        product_path = os.path.abspath(os.path.join(DB_PRODUCTS_DIR, payload["options"], f"{payload['options']}.json"))
        if not os.path.exists(product_path): raise CustomError("product path not exists")
        with open(product_path, "r", encoding="utf8") as f:
            data = json.load(f)
            if payload["options"] == "real-estate":
                for products in data.values():
                    for product in products:
                        if "id" in product.keys() and product["id"].lower() == payload["id"].lower(): return product
            elif payload["options"] == "miscellaneous":
                for id in data.keys():
                    if id.lower() == payload["id"].lower(): return data[id]
        # raise CustomError("id not in data")
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
    @staticmethod
    def write_product(payload):
        if not payload.get("options"): raise CustomError("Invalid option")
        product_path = os.path.abspath(os.path.join(DB_PRODUCTS_DIR, payload.get("options"), f"{payload.get('options')}.json"))
        if not os.path.exists(product_path): raise CustomError(f"Ivalid data with path: [{product_path}]")
        
        images_dir_path = os.path.abspath(os.path.join(DB_PRODUCTS_DIR, payload.get("options"), "images"))
        if not os.path.exists(product_path): raise CustomError(f"Ivalid images director with path: [{product_path}]")
        product_image_dir = os.path.abspath(os.path.join(images_dir_path, payload.get("id")))
        if not os.path.exists(product_image_dir): os.mkdir(product_image_dir)
        for index, image in enumerate(payload.get("images")):
            ext_file = image.split(".")[-1]
            shutil.copy(image, os.path.abspath(os.path.join(product_image_dir, f"{payload.get("id")}_{index}.{ext_file}")))
        payload["images"] = product_image_dir
        with open(product_path, "r", encoding="utf8") as f:
            data = json.load(f)
        if payload.get("options") == "real-estate":
            data.get(payload.get("type")).append(payload)
            with open(product_path, "w", encoding="utf8") as f:
                json.dump(data, f, indent=4)
        elif payload.get("options") == "miscellaneous":
            data.get("misc").append(payload)
            with open(product_path, "w", encoding="utf8") as f:
                json.dump(data, f, indent=4)
        else: raise CustomError("Invalid option")

class CustomError(Exception):
    pass

if __name__ == "__main__":
    ProductHandler.read("real-estate")