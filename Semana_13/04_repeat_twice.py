#1. Cree una función que imprima “Hola, [nombre]” dos veces:
#Cree un decorador `@repeat_twice` que haga que la función decorada se ejecute dos veces seguidas, 
# con los mismos argumentos.

#"Hola, Jeancarlos"
#"Hola, Jeancarlos"

class Person:

    def __init__(self, name):
        self.name = name
    
    def repeat_twice(func):
        def wrapper(user, *args):
           for i in range(2):
               func(user,*args)
        return wrapper

    @repeat_twice
    def print_user_name(user):
        print(f'Hola, {user.name}')


p = Person("Jeancarlos")
p.print_user_name()