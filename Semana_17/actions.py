

class actionHandler:

    def __init__(self):
        self.movement_list = []
    
    def add_movement(self,movement):
        self.movement_list.append(movement)
    
    def read_movement_list(self):
        for movement in self.movement_list:
             print(f" Full date: {movement.date}")
    

        
        