
def find_vowels(phrase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    cont = 0
    for index in phrase:
        for aux in range(0,len(vowels)):
            if index == vowels[aux]:
                cont = cont + 1
    return cont


text = 'Hola Mundo'
print(find_vowels(text))
