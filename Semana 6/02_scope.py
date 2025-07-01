#2. Experimente con el concepto de scope:
#1. Intente accesar a una variable definida dentro de una función desde afuera.
#2.  Intente accesar a una variable global desde una función y cambiar su valor.
def show_cartoon_name():
  name = 'Goku'
  print(f'Name: {name}')


def modify_cartoon_name():
   print(f'New Value: {name}')


def delete_cartoon_name_global(list):
   delete_item = list.pop(3)
   print(f'{list}')
   print(f'Deleted item: {delete_item} ')


def main():
  power_puff = ['Bellota', 'Burbuja', 'Bombon', 'Mojo jojo']
  show_cartoon_name()
  delete_cartoon_name_global(power_puff)


if __name__ == "__main__":
  main()