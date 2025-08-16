
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2*(self.width + self.height))
      

width = int(input('Enter the width value: '))
height = int(input('Enter the height value: '))

if width > 0 < height:
    rectangle = Rectangle(width,height)
    rectangle_area = rectangle.get_area()
    rectangle_perimeter = rectangle.get_perimeter()

    print(f'Area: {rectangle_area}')
    print(f'Perimeter: {rectangle_perimeter}')
else:
    print('Invalid Number, negative values are not allowed')

            


