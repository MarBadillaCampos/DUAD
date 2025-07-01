#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”
def invertir_string(my_string):
    record = ' '
    for index in range(len(my_string) -1, -1 , -1):
        record = record + my_string[index]
    return record


def main():
    my_string = 'Hola mundo'
    print(invertir_string(my_string))
    

if __name__ == '__main__':
    main()