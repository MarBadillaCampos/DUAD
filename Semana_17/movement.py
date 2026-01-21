
class Movement:
    def __init__(self,date,category,cost,mv_type):
        self.date = date
        self.category = category
        self.cost = cost
        self.mv_type = mv_type
    
    def to_dict(self):
        return {
            "date" : self.date,
            "category" : self.category,
            "cost" : self.cost,
            "mv_type" : self.mv_type
        }