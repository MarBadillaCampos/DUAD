#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
def is_upper_case(my_word):
   counter = 0
   for word in my_word:
      if word.isupper():
         counter = counter + 1
   return counter


def is_lower_case(my_word):
   counter = 0
   for i in my_word:
      if i.islower():
         counter = counter + 1
   return counter


def print_counter(upper_counter,lower_counter):
   print(f'There´s {upper_counter} upper cases and {lower_counter} lower cases')


def main():
   my_string = 'I love Nación Sushi'
   is_upper_case(my_string)
   upper_case_word = is_upper_case(my_string)
   lower_case_word = is_lower_case(my_string)
   print_counter(upper_case_word,lower_case_word)
   
   
if __name__ == "__main__":
  main()