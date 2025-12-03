
def sort_bubble(my_list):
    for out_index in range(0,len(my_list) - 1 ):
        for index in range(0, len(my_list) - 1 - out_index):
            current_value = my_list[index]
            next_value = my_list[index + 1]

            if current_value > next_value:
                my_list[index] = next_value
                my_list[index + 1] = current_value

def validate_list(my_list):
      size = len(my_list)
      if size == 0:
          print('Empty List') 
      else:
        for index in range(size):
            value = my_list[index]
            if not (isinstance(value, (int))):
                raise ValueError ('Only numbers are allowed')
        sort_bubble(my_list)


happy_path = [18, -11, 68, 6, 32, 53, -2]
case_one = [18,'a', 68, 6, 32, 53, -2]
empty_list = []

validate_list(happy_path)
validate_list(case_one)
validate_list(empty_list)

print(happy_path)
print(case_one)



