from movement import Movement

class actionHandler:

    def __init__(self):
        self.movement_list = []
    
    def add_movement(self,movement):
        self.movement_list.append(movement)
    
    def read_movement_list(self):
        for values in self.movement_list:
           values.display()
