#Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
# y le pida al usuario adivinar ese número. 
# El algoritmo no debe terminar hasta que el usuario adivine el numero.
secret_num = 5
user_input = 0
counter = 1
try:
    while secret_num != user_input:
        user_input = int(input("Ingrese un numero entero entre 1 y 10: "))
    counter = counter + 1 
    print("Felicidades!! Adivinó el Número")
    
except ValueError:
    print("Solo ingrese números validos ")