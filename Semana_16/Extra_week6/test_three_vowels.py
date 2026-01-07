from three_vowels import find_vowels


def test_find_vowels():
    input_string = 'Hola Mundo en python'
    result = find_vowels(input_string)
    assert result == 6

def test_find_vowels_no_vowels():
    input_string = 'rhythm'
    result = find_vowels(input_string)
    assert result == 0

def test_find_vowels_uppercase():
    input_string = 'AEIOU'
    assert find_vowels(input_string) == 0 
