import os, csv
#Export Data
class DataHandler:
    def __init__(self):
        pass
             
    def validate_data(self,file_path):
        return os.path.exists(file_path)
    
    def create_csv(self,file_path,headers):
        if not self.validate_data(file_path):
            with open(file_path, 'w', newline='',encoding='utf-8') as file:
                 writer = csv.DictWriter(file, headers)
                 writer.writeheader()
            print("The file was successfully created.")
        else:
            print('This File is already exists, information added it')

    def write_csv_file(self, file_path, headers, data):
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers)
            for row in data:
                writer.writerow(row)

 #Import   
    def read_csv_file_import(self,file_path):
        if self.validate_data(file_path):
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            for row in data:
                for key in ['spanish_score', 'english_score', 'social_score', 'science_score']:
                    try:
                        row[key] = int(row[key])
                    except ValueError:
                        row[key] = 0
            return data 
        else:
            print(f'This file [{file_path}] is not create yet.')
            return []
    
    def delete_item_from_list(self, import_list):
        for row in import_list:
            row.pop('average_grade', None)
        return import_list

    def read_my_import_list(import_list):
        for row in import_list:
            print(row)   

        
