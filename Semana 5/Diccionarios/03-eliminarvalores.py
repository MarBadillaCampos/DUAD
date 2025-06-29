#2. Cree un programa que use una lista para eliminar keys de un diccionario.
#    1. Ejemplos:
#   2. `list_of_keys = [’access_level’, ‘age’]`
#    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

list_of_employee = ['access_level', 'age']
employee = {
    'name' : 'John',
    'email' : 'john@ecorp.com',
    'access_level' : '5',
    'age' : '28'
}

for index in range(0,len(list_of_employee)):
    key = list_of_employee[index]
    if key in employee:
        employee.pop(key)

for key, value in employee.items():
    print(f'{key} : {value}')
