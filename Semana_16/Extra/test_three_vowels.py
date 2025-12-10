from three_vowels import find_vowels

def test_find_vowels():
    input_string = 'Hola Mundo en python'
    result = find_vowels(input_string)
    assert result == 6