from two_count_n_characters import read_list

def test_read_list():
    my_list = ['juan','julissa','gael','mar']
    number = 3
    result = read_list(my_list, number)
    assert result == ['juan','julissa','gael']