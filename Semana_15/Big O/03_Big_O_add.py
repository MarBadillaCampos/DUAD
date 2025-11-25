#Version 1
def manual_add(n):
    result = 0 #O(1)
    for i in range(1, number + 1): #O(n)
        result += i #O(1)
    return result

#version 2
def add_formula(n):
    return number * (number + 1) // 2 #O(1)

10 *(10 + 1)

# Preguntas:
#    - ¿Qué versión usaría si `number = 1 000 000 000`? ¿Por qué?
# Version 2: Porque el algoritmo tiene menor complejidad que la version 1, da igual si el numero es 10 
# o 1 millon, el va a ejecutar solo 3 operaciones: multiplicacion, suma, division. Mientras que en la version 1
#tendria que hacer una cantidad n de iteraciones lo que consume mayor recurso. 