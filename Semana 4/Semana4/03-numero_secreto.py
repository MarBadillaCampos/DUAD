#Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
import random
num_random = random.randint(1, 10)
num_user = 0
try:
    while num_user != num_random:
        num_user = int(input("Ingrese un número entre 1 y 10: "))
        if num_user < 1 or num_user > 10:
         print("¡Ese número está fuera del rango! Intente nuevamente.")
        elif num_user != num_random:
            print("No es el número secreto. Intente otra vez.")
    print("¡Adivinó el número!")
except ValueError:
    print("Error: Por favor, ingrese solo números enteros")





    

