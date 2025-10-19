#02-Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
# y arroje una excepción de no ser así.

class Number:
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def valid_numbers(func):
        def wrapper(num, *args):
            if not (isinstance(num.num1, (int)) and isinstance(num.num2, (int))):
                raise ValueError('Only Numbers are allowed it')
            return func(num, *args)
        return wrapper
    
    @valid_numbers
    def sum(self):
        return self.num1 + self.num1

n = Number(2,7)
print(n.sum())
