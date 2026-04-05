from category import Category

class categoryHandler:

    def __init__(self):
        self.category_color = {}

    def check_category(self,category_name, color):
        category_name = category_name.strip().lower()

        if category_name in self.category_color:
            category =  self.category_color[category_name]
            category.color = color
            return category
        
        new_category = Category(category_name,color)
        self.category_color[category_name] = new_category
        return new_category

    
    def read_category_color(self):
        for category in self.category_color.values():
            category.display()
