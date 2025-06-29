#3. Cree un algoritmo que le pida un numero al usuario, 
# y realice una suma de cada numero del 1 hasta ese número ingresado. 
# Luego muestre el resultado de la suma.
#    1. 3 → 6 (1 + 2 + 3)
#    2. 5 → 15 (1 + 2 + 3 + 4 + 5)
#    3. 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)
counter = 0
result = 0
num_user = 0

try: 
    num_user = int(input("Ingrese un numero: "))

    while counter <= num_user:
        result = result + counter
        counter = counter + 1

    print (f"{result}")
except ValueError:
    print("Ingrese un número válido")
