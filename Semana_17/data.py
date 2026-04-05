from pathlib import Path
import os,csv
from movement import Movement

class DataHandler:
    def __init__(self):
        pass

#CSV
    def validate_data(self,file_path):
            return os.path.exists(file_path)
    
    def save_movements(self, file_path, movement_list, income_value, expense_value, profit):
        with open(file_path,'w',newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["today_date","category_name","color","cost","mv_type"])

            writer.writeheader()
            for movement in movement_list:
                writer.writerow(movement.to_dict())
            
            file.write("\n")
            file.write("Totals\n")
            file.write(f"Income: {income_value}\n")
            file.write(f"Expense: {expense_value}\n")
            file.write(f"Net prof: {profit}\n")

    def read_movements(self,file_path): 
        if self.validate_data(file_path):
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
            
            cleaned_data = []
                
            for row in data:
                 if not row.get("today_date") or not row.get("mv_type"):
                    continue
                    
                 try:
                     row["cost"] = float(row["cost"])
                 except (ValueError,TypeError):
                    continue
                 
                 cleaned_data.append(row)
            return cleaned_data
        else:
            print(f'This file [{file_path}] is not create yet.')
            return []

        
    def load_movements(self, file_path, category_handler):
        data = self.read_movements(file_path)
        movements = []

        for row in data:
            if row["today_date"]: 
                category = category_handler.check_category(
                    row["category_name"],
                    row["color"],
                )

                movement = Movement(
                    row["today_date"],
                    category,
                    row["cost"],
                    row["mv_type"]
                )
                movements.append(movement)

        return movements
    
    def get_income_list(self, movement_list):
        filtered_income_records = []

        for movement in movement_list:
            if movement.mv_type == 'ingreso':
                filtered_income_records.append(movement)
        return filtered_income_records
    
    def get_expense_list(self, movement_list):
        filtered_expense_records = []
        
        for movement in movement_list:
            if movement.mv_type == 'gasto':
                filtered_expense_records.append(movement)
        return filtered_expense_records