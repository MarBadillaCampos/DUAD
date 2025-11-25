

def bubble_sort(my_list):
    for out_index in range(0, len(my_list) - 1): #O(n^2)
        for index in range(0, len(my_list) - 1 - out_index): #O(n^2)
            current_value = my_list[index] #O(1)
            next_value = my_list[index + 1] #O(1)

            if current_value > next_value: #O(1)
                my_list[index] = next_value #O(1)
                my_list[index + 1] = current_value #O(1)



happy_path = [18, -11, 68, 6, 32, 53, -2]
bubble_sort(happy_path)
print(happy_path)