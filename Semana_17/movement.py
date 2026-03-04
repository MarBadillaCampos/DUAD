from datetime import datetime
class Movement:
    def __init__(self,today_date,category,cost,mv_type):
        if isinstance(today_date, str):
            self.today_date = datetime.strptime(today_date, "%d-%m-%Y").date()
        else:
            self.today_date = today_date
        self.category = category
        self.cost = cost
        self.mv_type = mv_type
    
    def display(self):
        print(
            f"today_date: {self.today_date} | "
            f"category: {self.category} | "
            f"cost: {self.cost} | "
            f"mv_Type: {self.mv_type}"
        )
    
    def to_dict(self):
        return {
            "today_date": self.today_date.strftime("%d-%m-%Y"), #date to String 
            "category": self.category,
            "cost": self.cost,
            "mv_type": self.mv_type
        }
