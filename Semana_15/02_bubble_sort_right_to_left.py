def bubble_sort_right_to_left(list_to_sort):
    for outer_index in range(len(list_to_sort) - 1):
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index - 1]
            
            if current_element < next_element:
             list_to_sort[index] = next_element
             list_to_sort[index - 1] = current_element   

my_test_list = [9,8,7,6,5,4,3,2,1]
print(f"Before Bubble Sort {my_test_list}")
bubble_sort_right_to_left(my_test_list)
print(f"After Bubble Sort From Right To Left' {my_test_list}")

