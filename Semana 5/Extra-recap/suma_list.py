#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41
def sumar_list(my_list):
    record = 0
    for index in range(0,len(my_list)):
        record = record + my_list[index]
    return record


def main( ):
    my_list_numbers = [4, 6, 2, 29]
    print(sumar_list(my_list_numbers))


if __name__ == '__main__':
    main()