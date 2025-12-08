from week_6 import sum_list,back_string

def test_sum_list():
    input_list = [1,2,3]
    result = sum_list(input_list)
    assert result == 6

def test_back_string():
    input_string = 'hola'
    result = back_string(input_string)
    assert result == 'aloh'