#3. Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.
#    1. *Ejemplos*:
#        1. 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
#        2. 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
#        3. 1, 1, 1, 1, 1, 2 → 84.4% mujeres y 16.6% hombres
girls_counter = 0
boys_counter = 0
counter = 1

try: 
    while counter <= 6:
        gender = int(input("Ingrese el sexo de la persona [1 = Mujer o 2 = Hombre]: "))
        if gender == 1: 
            girls_counter = girls_counter + 1

        elif gender == 2: 
            boys_counter = boys_counter + 1

        counter = counter + 1

    girls_average = (girls_counter / 6) * 100
    boys_average = (boys_counter / 6) * 100

    print("------***** Resultados*****------")
    print(f"Porcentaje de Mujeres: {girls_average}")
    print(f"Porcentaje de Hombres: {boys_average}")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros")
