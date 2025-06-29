#Cree un programa que me permita ingresar información de `n` cantidad de videogames y 
# los guarde en un archivo `csv` separado por Tabulacion
#    1. Debe incluir:
#       1. Nombre
#        2. Género
#        3. Desarrollador
#        4. Clasificación
import csv

def get_input():
    return input("¿Do you want to add a new Video Game? [Yes] or [Not]: ").strip().lower()

def ask_information():
    name = input("Name: ")
    genre = input("Genre: ")
    developer = input("Developer: ")
    category = input('Category: ')
    return {"name": name, "genre": genre, "developer": developer, "category": category}


def write_csv_file(file_path, data, headers):
    with open(file_path,'w',encoding='utf-8',newline='') as file:
        writer = csv.DictWriter(file, headers,delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

def read_csv_file(file_path):
    with open(file_path,'r') as file:
        reader = csv.DictReader(file,delimiter='\t')
        for row in reader:
            print(row)

def main():
    video_games = []
    file_path = './csv/video_games_with_tab.csv'

    while True:
        option = get_input()

        if option == 'yes':
            game = ask_information()
            video_games.append(game)
        elif option == 'not':
            write_csv_file(file_path,video_games,video_games[0].keys())
            read_csv_file(file_path)
            break
        else:
            print("Invalid Option")

if __name__ == '__main__':
    main()
