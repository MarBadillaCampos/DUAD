from week_6 import sum_list,back_string,upper_case,lower_case,create_list,sorted_list,list_to_String,validate_is_prime
#3
def test_sum_list():
    input_list = [1,2,3]
    result = sum_list(input_list)
    assert result == 6

#4
def test_back_string():
    input_string = 'hola'
    result = back_string(input_string)
    assert result == 'aloh'

#5
def test_validate_upper_case():
    input_string = 'Hola Mundo'
    result = upper_case(input_string)
    assert result == 2

def test_validate_lower_case():
    input_string = 'Hola Mundos'
    result = lower_case(input_string)
    assert result == 8

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

def test_validate_prime():
    input_string = [2,4,12,7,3,13, 55,78] 
    result = validate_is_prime(input_string)
    assert result == [2,7,3,13]