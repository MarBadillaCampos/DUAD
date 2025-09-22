
class Vehicle:
    def __init__(self,brand,year,):
        self._brand = brand #protected
        self._year = year #protected
    
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,new_year):
        self._year = new_year
    
    def get_info(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    @property
    def doors(self):
        return self._doors
    
    @doors.setter
    def set_doors(self, doors):
        self._doors = int(doors)
    
    def get_info(self):
        print(f'{self.brand} - {self.year} - {self.doors} doors')

class Motorcycle(Vehicle):

    def __init__(self, brand, year, category):
        super().__init__(brand, year)
        self._category = category

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        self._category = new_category
    

    def get_info(self):
        print(f'{self.brand} - {self.year} - Category: {self.category} ')



def main():
    vehicle1 = Car('Toyota', 2020, 4)
    vehicle2 = Car('Hyundai', 2015, 2)
    vehicle1.get_info()
    vehicle2.get_info()
    vehicle3 = Motorcycle('Honda', 2025, 'Sport')
    vehicle4 = Motorcycle('Yamaha', 2005, 'off-road')
    vehicle3.get_info()
    vehicle4.get_info()


if __name__ == "__main__":
    main()



