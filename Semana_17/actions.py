from movement import Movement
from datetime import datetime

class actionHandler:

    def __init__(self):
        self.movement_list = []
    
    def add_movement(self,movement):
        self.movement_list.append(movement)
    
    def read_movement_list(self):
        for values in self.movement_list:
           values.display()
    
    def create_list(self):
        aux_list = []
        for values in self.movement_list:
            today_date = values.today_date
            category = values.category
            cost = values.cost
            mv_type = values.mv_type
            new_list = [today_date,category,cost,mv_type]
            aux_list.append(new_list)
        return aux_list
    
    def filter_by_date(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date()

        filtered_records = []
        for movement in self.movement_list:
            if start_date <= movement.today_date <= end_date:
                filtered_records.append(movement)
        return filtered_records

          
    

