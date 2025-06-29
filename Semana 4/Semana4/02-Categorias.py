#2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un 
# bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

try:
    name = input("Ingrese su nombre: ")
    last_name = input("Ingrese su apellido: ")
    age = int(input("Ingrese su edad: "))

    print(f'{name}{last_name} Categoría = ')

    if  age <= 2: 
        print("Bebé")
    elif age > 2 and age <= 5:
        print ("Niño")
    elif age > 5 and age <= 12:
        print("Preadolescente")
    elif age>12 and age <= 18:
        print("Adolescente")
    elif age > 18 and age <=30:
        print("Adulto Joven")
    elif age > 30 and age <= 60:
        print("Adulto")
    else:
        print("Adulto Mayor")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros")

