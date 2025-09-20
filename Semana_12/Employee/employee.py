class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.salary = salary 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError("Negative input")
        self._salary = new_salary 

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
