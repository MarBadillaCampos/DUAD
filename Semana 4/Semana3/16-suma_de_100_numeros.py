#Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.
counter = 1
result = 0
try:
    while counter <= 100:
        user_input = int(input(f"Ingrese el numero {counter}: "))
        result = result + user_input
        counter = counter + 1
    print(f"La suma total es de: {result}")

except ValueError:
    print("")
