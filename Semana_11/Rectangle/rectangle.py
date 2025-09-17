
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2*(self.width + self.height))
class Menu:
    def __init__(self):
        pass

    def ask_width(self):
        while True:
            try:
                width = int(input(f'Enter the width value: '))
                if 0 <= width:
                    return width
                else:
                    print(f'Value must positive Please try again')
                    
            except ValueError:
                print("Invalid input. Please enter a numeric value. Please try again")
    
    def ask_height(self):
        while True:
            try:
                height = int(input(f'Enter the height value: '))
                if 0 <= height:
                    return height
                else:
                    print(f'Value must positive Please try again')
                    
            except ValueError:
                print("Invalid input. Please enter a numeric value. Please try again")

class Main:
    def __init__(self):
        pass

    def action(self):
        menu_handler = Menu()
        width = menu_handler.ask_width()
        height = menu_handler.ask_height()
        rectangle = Rectangle(width,height)
        rectangle_area = rectangle.get_area()
        rectangle_perimeter = rectangle.get_perimeter()

        print(f'Area: {rectangle_area}')
        print(f'Perimeter: {rectangle_perimeter}')

                

main = Main()
main.action()



            


