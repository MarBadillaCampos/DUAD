import os, csv
#Export Data

class DataHandler:
    def __init__(self):
        pass
             
    def validate_export_data(self,file_path):
        return os.path.exists(file_path)
    
    def create_csv(self,file_path,headers):
        if not self.validate_export_data(file_path):
            with open(file_path, 'w', newline='',encoding='utf-8') as file:
                 writer = csv.DictWriter(file, headers)
                 writer.writeheader()
        else:
            print('Archivo existente')

    def write_csv_file(self,file_path,headers,data):
        with open(file_path,'w',newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, headers)

            file.seek(0,2)
            if file.tell() == 0:
                writer.writeheader()
            
            for row in data:
                writer.writerow(row)
    
    def read_csv_file_import(self,file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            for row in data:
                for key in ['spanish_grade', 'english_grade', 'social_grade', 'science_grade']:
                    try:
                        row[key] = int(row[key])
                    except ValueError:
                        row[key] = 0
        return data 
    
    def delete_item_from_list(self, import_list):
        for row in import_list:
            row.pop('average_grade',None)
        return import_list

    def read_my_import_list(import_list):
        for row in import_list:
            print(row)   

        
