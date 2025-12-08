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


word = 'I love Nación Sushi'
print(f'There is {upper_case(word)} upper cases and {lower_case(word)} lower cases')