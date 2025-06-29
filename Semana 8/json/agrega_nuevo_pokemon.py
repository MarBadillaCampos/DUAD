import json


def import_data(file_path):
        with open(file_path, "r") as file:
            return json.load(file)


def save_data(file_path, list):
    with open(file_path, "w") as file:
        json.dump(list, file, indent=4)

def get_input():
    return input("Would you like to add a new Pokemon? [Yes] or [Not]: ").strip().lower()

def ask_information():
    language = input("Language: ")
    name = input("Name: ")
    category = input("Type: ")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))
    
    return {
        "name": {language: name},
        "type": [category],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

def main():
    file = "./json/pokemones.json"
    pokemones = import_data(file)

    while True:
        option = get_input()

        if option == 'yes':
            pokemon = ask_information()
            pokemones.append(pokemon)
            save_data(file, pokemones)
        elif option == 'not':
            print(json.dumps(pokemones, indent=4))
            break
        else:
            print("Invalid Option")

if __name__ == '__main__':
    main()
