#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41
def sum_list(my_list):
    value = 0
    for index in range(0, len(my_list)):
        value = value + my_list[index]
    return value


#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”

def back_string(phrase):
    aux_string = ""
    for index in range(len(phrase)-1,-1,-1):
     aux_string = aux_string + phrase[index]
    return aux_string


#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def upper_case(phrase):
   upper_cont = 0
   for index in phrase:
      if index.isupper():
         upper_cont = upper_cont + 1
   return upper_cont


def lower_case(phrase):
   lower_cont=0
   for index in phrase:
        if index.islower():
            lower_cont = lower_cont + 1
   return lower_cont


#word = 'Hola Maria'
#print(f'There is {upper_case(word)} upper cases and {lower_case(word)} lower cases')


#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual 
#   pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → 
# “computadora-funcion-monitor-python-variable”

def create_list(phrase):
   my_new_list = []
   new_string = phrase.split('-')
   for index in new_string:
      my_new_list.append(index) 
   return my_new_list

def sorted_list(my_list):
    my_list.sort()
    return my_list

def list_to_String(my_list):
    record = ''
    for index in range(0, len(my_list)):
        record = record + my_list[index]
        if index != len(my_list)-1:
            record = record + '-'  
    return record
      
#phrase = "python-variable-funcion-computadora-monitor"
#my_list = create_list(phrase)
#print(my_list)
#sorted_aux_list = sorted_list(my_list)
#print(list_to_String(sorted_aux_list))

#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.


def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    sqrt = int(number**0.5) + 1
    for i in range(3, sqrt, 2): 
        if number % i == 0:
            return False

    return True


def validate_is_prime(my_list):
    prime_list = []
    for index in range(0, len(my_list)):
        if isPrime(my_list[index]) == True : 
            prime_list.append(my_list[index])
    return prime_list

my_list = [1, 4, 6, 7, 13, 9, 67]
validate_is_prime(my_list)


   