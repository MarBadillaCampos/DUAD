class Employee:
    def __init__(self, name, salary):
        self.__name = name #private
        self.__salary = salary #private

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError("Negative input")
        self.__salary = new_salary 

    def promote(self, value):
        increase = int(self.salary * value)
        self.salary += increase  
        return self.salary


def main():
    try:
        employee = Employee('mar', 1000)  
        employee.promote(0.1)
        print(employee.salary)


        employee1 = Employee('mar', -500)  
        employee1.promote(0.1)
        print(employee1.salary)

    except ValueError as e:
        print(f"Error: {e}")  


if __name__ == "__main__":
    main()
