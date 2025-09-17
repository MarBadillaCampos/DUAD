
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.1416 * (self.radius**2)

def main():
    my_circle_one = Circle(5)
    print(f'First circle area :  {my_circle_one.get_area():.2f} ')


    my_circle_two = Circle(25)
    print(f'Second circle area :  {my_circle_two.get_area():.2f} ')

if __name__ == '__main__':
    main()