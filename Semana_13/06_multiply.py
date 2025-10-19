#2. Cree una función que se llame `multiply`, la cual obtiene dos valores y los multiplica entre si
#A esta función  se le debe combinar dos decoradores:
#    - `@log_call`: imprime el nombre de la función, los argumentos, fecha actual y el retorno
#    - `@validate_numbers`: revisa que todos los argumentos sean numéricos

from datetime import datetime

class MultiPly:

    def __init__(self):
        pass

    def validate_numbers(func):
        def wrapper(self, *args):
            if not all(isinstance(x,(int)) for x in args):
                raise ValueError("Only Numbers are allowed")
            return func(self, *args)
        return wrapper

    def log_call(func):
        def wrapper(self, *args):
            result = func(self, *args)
            print(f"Función: multiply")
            print(f"Args: {args}")
            print(f"Date: {datetime.now()}")
            print(f"Result: {result}")
            return result
        return wrapper

    @log_call
    @validate_numbers
    def multiply(self, num1, num2):
        return num1 * num2

mtp = MultiPly()
resultado = mtp.multiply(10, 5)
