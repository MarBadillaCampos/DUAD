
#Cree una función que reciba un texto y un carácter, 
# y retorne cuántas veces aparece ese carácter en el texto
#```python
#programacion
#Ingrese el carácter que desea buscar: o
#Se a encontrado 2 veces el carácter

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