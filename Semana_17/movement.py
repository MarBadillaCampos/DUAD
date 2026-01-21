
class Movement:
    def __init__(self,date,category,cost,mv_type):
        self.date = date
        self.category = category
        self.cost = cost
        self.mv_type = mv_type
    
    def display(self):
        print(
            f"Date: {self.date} | "
            f"Category: {self.category} | "
            f"Cost: {self.cost} | "
            f"Type: {self.mv_type}"
        )
