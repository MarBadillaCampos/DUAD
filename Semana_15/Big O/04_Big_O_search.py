def linear_search(my_list, target):
    for item in my_list: #O(n)
        if item == target: #O(1)
            return True
    return False


#my_list1 = [1,2,3,4,5]
#my_list = [5,4,3,2,1]
#print(linear_search(my_list, 3))



def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1 #O(1)
    while low <= high: # O(log n)
        mid = (low + high) // 2 #O(1)
        if my_list[mid] == target: #O(1)
            return True
        elif my_list[mid] < target: #O(1)
            low = mid + 1 #O(1)
        else:
            high = mid - 1 #O(1)
    return False

my_list = [8, 6, 4, 2, 10, 12, 14]

print(binary_search(my_list, 4))

#¿Cuál es la complejidad de cada algoritmo?
#Linear Search es una complejidad O(n) 
#Binary_search es O(log n) 


#- ¿En qué condiciones conviene usar cada uno?
# Linear Search se utiliza cuando la lista no esta ordenada y no se necesita una lista muy grande. (Busqueda simple) 
# Cuando la lista esta ordenada 


#- ¿Qué pasa si la lista no está ordenada?
#Linear Search no tendra ningun problema en recorrer la lista si no esta ordenada. 