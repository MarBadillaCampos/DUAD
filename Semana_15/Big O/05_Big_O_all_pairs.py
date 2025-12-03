def print_all_pairs(my_dict):
    for key1 in my_dict: #O(n)
        for key2 in my_dict: #O(n^2)
            print(f" Este es el total{key1}-{key2}") #O(1)

#- Preguntas:
#    - ¿Cuál es la complejidad temporal?
#               O(n^2)
#    - ¿Cuanto dura si hay `1` millón de claves?
#       Seguiría siendo O(n^2) asi el diccionario tenga 1 millon de claves. 

