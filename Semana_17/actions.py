from movement import Movement

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
            date = values.date
            category = values.category
            cost = values.cost
            mv_type = values.mv_type
            new_list = [date,category,cost,mv_type]
            aux_list.append(new_list)
        return aux_list

          
    

