
class Category:
    

    def __init__(self,category_name, color):
        self.category_name = category_name
        self.color = color
  
    def display(self):
        print(
            f"category_name: {self.category_name} "
        )