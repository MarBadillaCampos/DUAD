from pathlib import Path
import os,csv
from movement import Movement

class DataHandler:
    def __init__(self):
        pass

#CSV
    def validate_data(self,file_path):
            return os.path.exists(file_path)
    
    def write_csv_file(self,file_path, movement):
        with open(file_path,'w',newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["today_date","category","cost","mv_type"])

            writer.writeheader()
            
            for movement in movement:
                writer.writerow(movement.to_dict())
    

    def read_csv_file_import(self,file_path):
        if self.validate_data(file_path):
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            for row in data:
                for key in ["cost"]:
                    try:
                        row[key] = float(row[key])
                    except ValueError:
                        row[key] = 0
            return data 
        else:
            print(f'This file [{file_path}] is not create yet.')
            return []
        
    def load_movements(self, file_path):
        data = self.read_csv_file_import(file_path)
        movements = []
        for row in data:
            movement = Movement(
                row["today_date"],
                row["category"],
                row["cost"],
                row["mv_type"]
            )
            movements.append(movement)

        return movements