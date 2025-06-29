#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual 
#   pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → 
# “computadora-funcion-monitor-python-variable”

def delete_dashes(my_string):
    result = ' '
    for value in my_string:
        if value == '-':
           result = result + ','
        else:
            result = result + value
    result = result.strip()
    return result              


def create_list(my_string):
    my_list = my_string.split(',')
    return my_list


def sort_list(my_list):
    return sorted(my_list)


def list_to_String(my_list):
    record = ' '
    for index in range(0,len(my_list)):
        record = record + my_list[index]
        if index != len(my_list)-1:
            record = record + '-'  
    return record


def main():
    my_string = "python-variable-funcion-computadora-monitor"
    my_new_string = delete_dashes(my_string)
    new_list = create_list(my_new_string)
    my_sorted_list = sort_list(new_list)
    second_string = list_to_String(my_sorted_list)
    print(second_string)
    

if __name__ == '__main__':
    main()  