#1. Cree un decorador `@requires_login` que:
#    - Verifique si la variable global `user_logged_in` es `True`
#    - Si no lo es, debe lanzar una excepción `"Usuario no autenticado"`
#    - Si lo es, la función decorada se ejecuta normalmente
#    - Ejemplo:
#        - Entrada:

user_logged_in = True

class Person:

    def __init__(self, name):
        self.name = name

    def requires_login(func):
        def wrapper(person, *args):
            if user_logged_in != True:
                raise ValueError(f'Usuario no autenticado')
            func(person,*args)
        return wrapper
    
    @requires_login
    def view_profile(person):
        print(f"Mostrando perfil del usuario {person.name}")

person = Person('Mar')
person.view_profile()