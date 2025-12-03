
def bubble_sort(sort_list):
    cont = 0
    swap = 0
    for out_index in range(0, len(sort_list) -1 ):
        cont = cont + 1
        for index in range(0, len(sort_list) - 1 - out_index):
            current_element = sort_list[index]
            next_element = sort_list[index + 1]
            print(f'-- Iteration {index}. Current Element: {current_element}, Next Element: {next_element}')

            if current_element > next_element:
                print('Current element is bigger than the next element. Let’s swap them...')
                swap = swap + 1
                sort_list[index] = next_element
                sort_list[index + 1] = current_element
    print(f'Iterations: {cont}')
    print(f'Swapped: {swap}')

my_list = [5, 4, 3, 2, 1]
bubble_sort(my_list)
print(my_list)
 #Duda