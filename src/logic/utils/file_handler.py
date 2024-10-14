import os
MY_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.abspath(os.path.join(MY_DIR, os.path.pardir, os.path.pardir, ))
DB_DIR = os.path.abspath(os.path.join(SRC_DIR, os.path.pardir, "bin", "db"))
DB_PRODUCT_DIR = os.path.abspath(os.path.join(DB_DIR, "products"))
DB_TEMPLATE_DIR = os.path.abspath(os.path.join(DB_DIR, "templates"))

class FileHandler():
    @staticmethod
    def create_dir(_path):
        current_dir = ""
        for dir_name in _path.split("/"):
            current_dir += dir_name + "/"
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
        return _path
    
    @staticmethod
    def find_data_file(_path):
        current_path = _path
        for root, dirs, files in os.walk(current_path):
            print(f"root: {root} - dirs: {dirs} - files: {files}")

    @staticmethod
    def get_file_paths_of_data():
        results = []
        for root, dirs, files in os.walk(DB_PRODUCT_DIR):
            for file in files:
                file_ext = file.split(".")[-1].lower()
                if file_ext == "json":
                    results.append(os.path.abspath(os.path.join(root, file)))
        return results

    @staticmethod
    def get_path_of_file_data(name):
        for root, dirs, files in os.walk(DB_PRODUCT_DIR):
            for file in files:
                file_name = file.split(".")[0].lower() 
                file_ext = file.split(".")[-1].lower()
                if file_ext == "json" and file_name == name:
                    return os.path.abspath(os.path.join(root, file))
    @staticmethod
    def get_paths_of_file_data():
        file_paths = []
        for root, dirs, files in os.walk(DB_PRODUCT_DIR):
            for file in files:
                file_ext = file.split(".")[-1].lower()
                if file_ext == "json":
                    file_paths.append(os.path.abspath(os.path.join(root, file)))
        return file_paths
        
    @staticmethod
    def get_file_names_of_data():
        results = []
        for root, dirs, files in os.walk(DB_PRODUCT_DIR):
            for file in files:
                file_name = file.split(".")[0].lower() 
                file_ext = file.split(".")[-1].lower()
                if file_ext == "json":
                    results.append(file_name)
        return results