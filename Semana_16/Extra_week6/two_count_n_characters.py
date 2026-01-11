

#Cree una función que reciba una lista de palabras y un número n, y 
# retorne una nueva lista con solo las palabras que tengan más de n letras
#["cielo", "sol", "maravilloso", "día"]
#"Ingrese el numero de letras minimas en la palabra: " 4
#["cielo", "maravilloso"]


def ask_for_list_values():
    new_list = []
    option = int(input('How many values would you like to add '))
    for index in range(0,option):
        value = input(f'Add your value number {index} ')
        new_list.append(value)
    return new_list

def ask_number():
    number = int(input('Enter the minimum number of letters '))
    return number

def read_list(my_list, number):
    new_list = []
    for index in range(0,len(my_list)):
        if my_list[index] == '':
            raise ValueError('Invalid Value')
        else:
            if len(my_list[index]) > number:
                new_list.append(my_list[index])

    return new_list


#my_list = ask_for_list_values()
#number = ask_number()
#print(f'currently List: {my_list}')
#print(f'custom list {read_list(my_list,number)}')

my_list = ["cielo", "sol", "maravilloso", "día"]
number = 15
print(read_list(my_list, number))
