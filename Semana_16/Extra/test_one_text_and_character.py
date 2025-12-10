from one_text_and_character import read_option

def test_ask_text():
    input_string = 'Gato de ojos verdes'
    character = 'o'
    result = read_option(input_string, character)
    assert result == 3

