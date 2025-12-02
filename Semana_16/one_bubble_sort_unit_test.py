
def bubble_sort(my_list):
    for out_index in range(0, len(my_list) - 1):
        for index in range(0, len(my_list) - 1 - out_index):
            current_value = my_list[index]
            next_value = my_list[index + 1]

            if current_value > next_value:
                my_list[index] = next_value
                my_list[index + 1] = current_value

    return my_list



#Version 2
def bubble_sort_version_2(my_list):
    if my_list is not None:
        for out_index in range(0, len(my_list) - 1):
            for index in range(0, len(my_list) - 1 - out_index):
                current_value = my_list[index]
                next_value = my_list[index + 1]

                if current_value > next_value:
                    my_list[index] = next_value
                    my_list[index + 1] = current_value
    raise ValueError('Empty_list')



