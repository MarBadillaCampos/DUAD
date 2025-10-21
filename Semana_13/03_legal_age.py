# 03- 3. Cree una clase de `User` que:
#    - Tenga un atributo de `date_of_birth`.
#    - Tenga un property de `age`.    
#    Luego cree un decorador para funciones que acepten un `User` como parámetro 
# que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
    date_of_birth: date
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        return (
            today.year - self.date_of_birth.year -
            ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        )
    
    def underage(func):
        def wrapper(user,*args):
            if user.age < 18:
                raise ValueError('User is UnderAge')
            return func(user, *args)
        return wrapper
    
    @underage
    def  validate_user(user):
            print(f'Legal User Age [ {user.age} ]')


my_user = User(date(2024,1,1))
my_user.validate_user()