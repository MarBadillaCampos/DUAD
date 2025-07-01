#7. Cree una función que acepte una lista de números y retorne una lista con los números 
# primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matemática para averiguar si un numero es primo, 
# y convierta a código. No busque el código, eso no ayudaría.
#    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, 
# revisar si cada numero es primo,
#  y agregarlo a otra lista). Así que lo mejor es agregar **otra función** 
# para revisar si el numero es primo o no.*

def is_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for index in range(2, num):
        if num % index == 0:
            return False
    return True


def primos_en_lista(lista):
    my_list = []
    for numero in lista:
        if is_primo(numero):
            my_list.append(numero)
    return my_list


def main():
    mi_lista = [1, 4, 6, 7, 13, 9, 67]
    print(primos_en_lista(mi_lista))


if __name__ == '__main__':
    main()




        




