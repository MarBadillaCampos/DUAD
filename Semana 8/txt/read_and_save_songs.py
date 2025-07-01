#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y 
# guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def read_collection(path):
    my_list = []
    with open(path) as file:
        for line in file.readlines():
            my_list.append(line)
        return my_list
            
def sort_list(my_list):
    return sorted(my_list)

def read_list(my_list):
    new_string = ' '
    for record in my_list:
        new_string = new_string + record
    return new_string.strip()

def add_to_new_file(path, text):
    with open(path, 'a') as file:
        file.write(text)

def read_second_file(path):
   with open(path) as file:
       for line in file.readlines():
           print(f'{line}')
       
def main():
    my_list = read_collection('./txt/read_songs.txt')
    my_sort_list = sort_list(my_list)
    my_new_string = read_list(my_sort_list)
    add_to_new_file('./txt/saved_songs.txt',my_new_string)
    read_second_file('./txt/saved_songs.txt')
    
if __name__ == '__main__':
    main()
