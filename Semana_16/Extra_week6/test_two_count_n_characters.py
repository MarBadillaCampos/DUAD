from two_count_n_characters import read_list,ask_number
import pytest

def test_read_list():
    my_list = ['juan','julissa','gael','mar']
    number = 3
    result = read_list(my_list, number)
    assert result == ['juan','julissa','gael']


def test_validate_empty_input():
    input_string = ["cielo", "", "maravilloso", "día"]
    input_number = 4
    with pytest.raises(ValueError):
        read_list(input_string,input_number)

def test_read_list_no_word_meets_condition():
    my_list = ['sol', 'mar', 'día']
    number = 5
    result = read_list(my_list, number)
    assert result == []