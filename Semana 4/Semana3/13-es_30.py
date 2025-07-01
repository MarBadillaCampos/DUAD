#3. Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “*Correcto*”. Sino, mostrar “*incorrecto*”.
#1. *Ejemplos*:
#       1. 23, 30, 768 → Correcto (hay un 30)
#        2. 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
#        3. 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)
try:
    first_num = int(input("Ingrese el primero número: "))
    second_num = int(input("Ingrese el segundo número: "))
    third_num = int(input("Ingrese el tercer número: "))
    result = first_num + second_num + third_num

    if first_num == 30 or second_num == 30 or third_num == 30 or result == 30:
        print("Correcto")
    else:
        print("Incorrecto")

except ValueError:
    print("Numero invalido")

