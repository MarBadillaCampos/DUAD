from calculator import Calculator
import pytest

#Positive cases
def test_validate_addition():
    calc = Calculator()
    num1 = 5
    num2 = 4
    result = calc.addition(num1,num2)
    assert result == 9

#Negative cases
def test_multiplication_negative_numbers():
    calc = Calculator()
    num1 = -5
    num2 = 4
    assert calc.multiplication(num1, num2) == -20

#subtraction zero cases
def test_subtraction_zero_case():
    calc = Calculator()
    num1 = 5
    num2 = 5
    assert calc.subtraction(num1, num2) == 0


#Divide cases
def test_validate_division():
    cal = Calculator()
    num1 = 10
    num2 = 2
    result = cal.divide(num1,num2)
    assert result == 5.0

def test_zero_division():
    cal = Calculator()
    num1 = 10
    num2 = 0
    with pytest.raises(ValueError):
        cal.divide(num1,num2)

def test_validate_string_input():
    cal = Calculator()
    num1 = 2
    num2 = 'cuatro'
    with pytest.raises(TypeError):
        cal.divide(num1,num2)