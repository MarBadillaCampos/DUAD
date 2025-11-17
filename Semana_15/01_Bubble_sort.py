
def bubble_sort(my_list):
    for out_index in range(0,len(my_list) - 1 ):
        for index in range(0, len(my_list) - 1 - out_index):
            current_element = my_list[index]
            next_element = my_list[index + 1]

            if current_element > next_element:
                my_list[index] = next_element
                my_list[index + 1] = current_element


my_list = [18, -11, 68, 6, 32, 53, -2]
bubble_sort(my_list)
print(my_list)
