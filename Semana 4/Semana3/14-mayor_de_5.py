#1. Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.
#    1. *Ejemplos*:
#        1. 4, 76, 43, 6, 8 → 76
#        2. 1, 2, 3, 6, 7 → 7
#        3. 2132, 4355, 1132, 2323, 1214 → 4355
num_mayor = 0
try:
    one_opt = int(input("Ingrese el valor del primer número: "))
    two_opt = int(input("Ingrese el valor del segundo número: "))
    three_opt = int(input("Ingrese el valor del tercer número: "))
    four_opt = int(input("Ingrese el valor del cuarto número: "))
    five_opt = int(input("Ingrese el valor del quinto número: "))

    num_mayor = one_opt
    if two_opt > num_mayor:
        num_mayor = two_opt
    if three_opt > num_mayor:
        num_mayor = three_opt
    if four_opt > num_mayor:
        num_mayor = four_opt
    if five_opt > num_mayor:
        num_mayor = five_opt
    print(f"{num_mayor}")

except ValueError:
    print()
