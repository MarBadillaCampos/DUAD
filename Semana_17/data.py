import json
from pathlib import Path

class DataHandler:
    def __init__(self):
        pass

#JSON
    def validate_path(self, file_path):
        folder = Path("./Semana_17/json")
        folder.mkdir(exist_ok=True)
        aux_file_path = folder / file_path

    
    def save_data(self,file_path, list):
        with open(file_path, "w") as file:
            json.dump(list, file, indent=4)
    
    def import_data(self,file_path):
        with open(file_path, "r") as file:
            return json.load(file)

#CSV