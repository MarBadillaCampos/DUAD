from one_bubble_sort_unit_test import bubble_sort, bubble_sort_version_2
import pytest

def test_bubble_sort_small_list():
    input_list = [5,4,3,2,1]
    result = bubble_sort(input_list)
    assert result == [1,2,3,4,5]

def test_bubble_sort_empty_list():
    input_list = []
    result = bubble_sort(input_list)
    assert result == []

def test_bubble_sort_empty_list_v2():
    input_list = []
    with pytest.raises(ValueError):
        bubble_sort_version_2(input_list)

def test_bubble_sort_bigger_list():
    input_list = list(range(100, 0 , -1))
    output_list = list(range(1, 101))
    result = bubble_sort(input_list)
    assert result == output_list
    
