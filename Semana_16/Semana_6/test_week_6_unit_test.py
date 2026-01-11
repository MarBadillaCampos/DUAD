from week_6 import sum_list,back_string,upper_case,lower_case,create_list,sorted_list,list_to_String,validate_is_prime
import pytest

#3
def test_sum_list():
    input_list = [1,2,3]
    result = sum_list(input_list)
    assert result == 6

def test_empty_list():
    input_list = []
    with pytest.raises(ValueError):
        sum_list(input_list)

def test_validate_list_values():
    input_list = ['-1', '2', '-3']
    with pytest.raises(ValueError):
        sum_list(input_list)
 

#4
def test_back_string():
    input_string = 'hola'
    result = back_string(input_string)
    assert result == 'aloh'

def test_valid_inputs():
    input_value = ''
    with pytest.raises(ValueError):
        back_string(input_value)

def test_valid_type_input():
    input_value = ['Hola', 'mundo', 'de', 'Python']
    with pytest.raises(ValueError):
        back_string(input_value)

#5
def test_validate_upper_case():
    input_string = 'Hola Mundo'
    result = upper_case(input_string)
    assert result == 2

def test_validate_upper_case_for_every_value():
    input_string = 'HOLA MUNDO'
    result = upper_case(input_string)
    assert result == 9

def test_validate_upper_case():
    input_string = 'Hola Mundo'
    result = upper_case(input_string)
    assert result == 2

def test_validate_lower_case():
    input_string = 'Hola Mundos'
    result = lower_case(input_string)
    assert result == 8


#6
def test_create_a_list():
    input_string = 'Hola Mundo parte dos'
    result = create_list(input_string)
    assert result == ['Hola Mundo parte dos']

def test_sorted_list():
    input_string = ['d','c','b','a']
    result = sorted_list(input_string)
    assert result == ['a','b','c','d']

def test_list_to_string():
    input_string = ['Hola', 'Mundo', 'tres']
    result = list_to_String(input_string)
    assert result == 'Hola-Mundo-tres'

#7
def test_validate_prime():
    input_string = [2,4,12,7,3,13, 55,78] 
    result = validate_is_prime(input_string)
    assert result == [2,7,3,13]

def test_validate_prime_input():
    input_string = [2,'4',12,7,3,'13', 55,78]
    with pytest.raises(ValueError):
        validate_is_prime(input_string)

def test_validate_negative_values():
    input_string = [2,4,-12,7,3,13, 55,78]
    with pytest.raises(ValueError):
        validate_is_prime(input_string)