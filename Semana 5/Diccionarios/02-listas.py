#1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, 
# y la otra para sus values.
#1. Ejemplos:
#2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#`list_b = [’Mar’, ‘Badilla’, ‘Software Engineer’]`
# output → `{’first_name’: ‘Mar’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`

key_list = ['first_name', 'last_name', 'role']
value_list = ['Mar','Badilla', 'Software Engineer']
both_values = {}

if len(key_list) == len(value_list):
    for index in range(0,len(key_list)):
        key = key_list[index]
        value = value_list[index]
        both_values[key] = value
    print(f"{both_values}")
else:
    print("Las listas son de diferente tamaño")






