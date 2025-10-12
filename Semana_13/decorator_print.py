class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def decorator_person(func):
        def wrapper(person, *args):
            print(f'Person First Name: {person.first_name}')
            print(f'Person Last Name: {person.last_name}')
            result = func(person, *args)
            print(f'Resultado: {result}')
            return result
        return wrapper

    @decorator_person
    def create_person(person, nationality):
        return f'{person.first_name} {person.last_name} es de {nationality}'

p = Person("Mar", "Badilla")
p.create_person("Costa Rica")


