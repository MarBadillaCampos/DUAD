#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos 
# los números que ingresó, seguido del numero ingresado más alto.
#    1. Ejemplos:
#    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. 
# El más alto fue 86.

num_list = []
max_num = None

try: 
    for index in range(0,10):
        user_input = int(input(f'Ingrese el numero {index}:'))
        num_list.append(user_input)
    print(f'{num_list}')
    max_num = num_list[0]

    for counter in range(0,len(num_list)):
        if max_num < num_list[counter]:
            max_num = num_list[counter]
    print(f'El número mas alto fue {max_num}')
except:
    print("Numero no valido ")