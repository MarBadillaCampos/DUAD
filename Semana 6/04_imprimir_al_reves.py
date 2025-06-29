#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”

def reverse_string(my_word):
   for index in range(len(my_word)-1,-1,-1):
    aux_string = my_word[index]
    print(f'{aux_string}')


def main():
   my_string = 'Hola Mundo'
   reverse_string(my_string)
   

if __name__ == "__main__":
  main()
