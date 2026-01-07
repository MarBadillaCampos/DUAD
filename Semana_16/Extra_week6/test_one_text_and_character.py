from one_text_and_character import read_option


def test_ask_text():
    input_string = 'Gato de ojos verdes'
    character = 'o'
    result = read_option(input_string, character)
    assert result == 3

def test_read_option_character_not_found():
    input_string = 'Perro'
    character = 'z'
    result = read_option(input_string, character)
    assert result == 0

def test_read_option_empty_text():
    input_string = ''
    character = 'a'
    result = read_option(input_string, character)
    assert result == 0