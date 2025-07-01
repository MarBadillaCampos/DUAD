#Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos.

counter = 1
num_mayor = 0
try:
    user_input = int(input("Ingrese un numero: "))
    num_mayor = user_input

    while counter <= 100:
        user_input = int(input("Ingrese un numero: "))
        counter = counter + 1
        if user_input > num_mayor:
            num_mayor = user_input
    print(f"El número Mayor es: {num_mayor}")

except ValueError:
    print("Número no valido")