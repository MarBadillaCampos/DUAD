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
            category_name = values.category.category_name
            color = values.category.color
            cost = values.cost
            mv_type = values.mv_type
            new_list = [today_date,category_name,color,cost,mv_type]
            aux_list.append(new_list)
        return aux_list
    
    def filter_by_date(self, start_date, end_date):
        filtered_records = []
        for movement in self.movement_list:
            if start_date <= movement.today_date <= end_date:
                filtered_records.append(movement)
        return filtered_records
    
    def get_total_income(self, income_list):
        total = 0
        for income_value in income_list:
            total = total + income_value.cost
        return total
    
    def get_total_expense(self, expense_list):
        total = 0
        for expense_value in expense_list:
            total = total + expense_value.cost
        return total
    
    def get_profit_value(self,income,expense):
        total = 0
        if income != 0 and expense != 0:
            total = income - expense
        if income == 0:
            total = expense
        if expense == 0:
            total = income
        return total 




    



          
    

