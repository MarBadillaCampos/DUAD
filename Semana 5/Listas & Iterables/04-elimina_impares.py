#4. Cree un programa que elimine todos los números impares de una lista.
#    1. Ejemplos:
#   2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
new_values_list = []

for index in range(0, len(my_list)):
    value = int(my_list[index])
    if value % 2 == 0:
        new_values_list.append(value)
print(new_values_list)
