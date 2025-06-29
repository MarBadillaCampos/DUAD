#3. Cree un programa que intercambie el primer y ultimo elemento de una lista. 
# Debe funcionar con listas de cualquier tamaño.
#   1. Ejemplos:
#   2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`
#   3. string2 = [5, 10, 15, 20,30,35,40,45 ]`


my_list = ['4', '3', '6', '1', '7']
#my_list = ['5', '10', '15', '20','30','35','40','45']
print("***Resultados***")
print(f'Resultados de la lista antes de ser modificada: {my_list}')
temp_opt = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp_opt


print(f'Resultados de la lista después de ser modificada: {my_list}')

    

