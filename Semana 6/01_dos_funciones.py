#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def print_string_one ():
    print("Esta es la cadena 1 ")
    print_string_two()


def print_string_two():
    print("Esta es la cadena 2")


def main():
  print_string_one ()


if __name__ == "__main__":
  main()
