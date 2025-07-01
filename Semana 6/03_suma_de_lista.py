#3. Cree una función que retorne la suma de todos los números de una lista.
#   1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41
def suma(my_list):
   total= 0
   for index in range(0,len(my_list)):
      total = total + my_list[index]
   print(f'{total}')

  
def main():
   my_list = [4, 6, 2, 29]
   suma(my_list)


if __name__ == "__main__":
  main()
