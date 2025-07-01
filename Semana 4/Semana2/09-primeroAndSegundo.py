#1. Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas 
# (`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.
#    1. Ejemplos:
#        1. A: 56, B: 32 → A: 32, B: 56
#        2. A: 24, B: 76 → A: 24, B: 76
#        3. A: 45, B: 12 → A: 12, B: 45
try:
    first_num = int(input("Ingrese el valor del primer dígito: "))
    second_num = int(input("Ingrese el valor del segundo dígito: "))
    if first_num > second_num:
       print(f"A:{second_num}, B:{first_num}")
    else:
        print(f"A:{first_num}, B:{second_num}")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros.")