#2. Cree un pseudocódigo que le pida un `tiempo en segundos`
# al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “*Mayor*”. Si es exactamente igual, muestre “*Igual*”.
#    1. *Ejemplos*:
#        1. 1040 → Mayor
#        2. 140 → 460
#        3. 600 → Igual
#        4. 599 → 1

time_sec = 0
try: 
    time_sec = int(input("Ingrese el tiempo en segundos: "))

    if time_sec > 600:
        print("Mayor")
    elif time_sec < 600:
        result = 600 - time_sec
        print(f"{result}")
    else:
        print("Igual")
except ValueError:
    print("Solo números enteros son validos")
    