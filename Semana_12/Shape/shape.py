from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radio = 0
        self.pi = 3.14

    def calculate_perimeter(self,radio):
        self.radio = radio
        perimeter = (2 * self.pi * self.radio)
        return perimeter
    
    def calculate_area(self, radio):
        self.radio = radio
        area = self.pi * (self.radio**2)
        return area

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.length_side = 0
    
    def calculate_perimeter(self,length_side):
        self.length_side = length_side
        perimeter = 4 * self.length_side
        return perimeter
    
    def calculate_area(self, length_side):
        self.length_side = length_side
        area = length_side * self.length_side
        return area

class  Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0
    
    def calculate_perimeter(self,width,height):
        self.width = width
        self.height = height
        perimeter = 2*(self.width + self.height)
        return perimeter
    
    def calculate_area(self,width,height):
        self.width = width
        self.height = height
        area = self.width * self.height
        return area
        
class Menu():
    def __init__(self):
        pass

    def ask_for_shape(self):
        while True:
            try: 
                shape = input('Do you want to calculate any Area & Perimeter 1-[Circle] 2-[Square] 3-Rectangle: ')
                if shape in ('1' '2' '3'):
                    return shape
                else:
                    raise ValueError ('Invalid Option, Try again')
            except ValueError as e:
                print(f'{e}')
    
    def ask_for_radio(self):
        while True:
            try:
                radio = int(input('Enter a radio value: '))
                if radio >= 0:
                    return radio
                else:
                    raise ValueError('Invalid Value, try again')
            except ValueError as e:
                print(f'{e}')
    
    def ask_for_length_side(self):
        while True:
            try:
                length_side = int(input('Add one length side value: '))
                if length_side >= 0:
                    return length_side
                else:
                    raise ValueError('Invalid option. Try again')
            except ValueError as e:
                print(e)
    
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
                




def main():
        menu_handler = Menu()
        circle = Circle()
        square = Square()
        rectangle = Rectangle()

        while True:
            option = menu_handler.ask_for_shape()
            if option == '1':
                radio = menu_handler.ask_for_radio()
                perimeter = circle.calculate_perimeter(radio)
                area = circle.calculate_area(radio)
                print(f'Perimeter Result: {perimeter} cm')
                print(f'Area Result: {area} cm')
            elif option == '2':
                length_side = menu_handler.ask_for_length_side()
                perimeter = square.calculate_perimeter(length_side)
                area = square.calculate_area(length_side)
                print(f'Perimeter Result: {perimeter} cm')
                print(f'Area Result: {area} cm')
            elif option == '3':
                width = menu_handler.ask_width()
                height = menu_handler.ask_height()
                perimeter = rectangle.calculate_perimeter(width,height)
                area = rectangle.calculate_area(width,height)
                print(f'Perimeter Result: {perimeter} cm')
                print(f'Area Result: {area} cm')
            else:
                break

if __name__ == '__main__':
    main()

