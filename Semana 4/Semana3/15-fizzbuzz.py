#2. Cree un diagrama de flujo que le pida un numero al usuario y muestre “*Fizz*” 
# si es divisible entre 3, “*Buzz*” si es divisible entre 5, y “*FizzBuzz*” 
# si es divisible entre ambos.
#1. *Ejemplos*:
#        1. 33 → Fizz
#        2. 25 → Buzz
#        3. 30 → FizzBuzz

try: 
    user_num = int(input("Ingrese un número: "))
    if user_num % 3 == 0 and user_num % 5 == 0:
       print("FizzBuzz")
    elif user_num % 3 == 0:
        print("Fizz")
    elif user_num % 5 == 0:
        print("Buzz")
    else:
        print("Número no divisible entre 3 ni entre 5")

except ValueError:
    print("Ingrese un número válido")