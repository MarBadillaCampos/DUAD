
def ask_text():
    text = input('Add your Text ')
    return text

def ask_character():
    character = input('Add your Character ')
    return  character 

def read_option(text,character):
    cont = 0
    for index in text:
        if index == character:
            cont = cont + 1
    return cont

#text_aux = ask_text()
#character_aux = ask_character()
#print(read_option(text_aux,character_aux))