import random_password
def test_ascii_range_string_97_100():
    #setup
    start = 97
    stop = 100
    expected = "abc"

    #invoke
    actual = random_password.create_ascii_range_string(start, stop)

    #analyze
    assert expected == actual

def test_uppercase_string():
    #setup
    expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #invoke
    actual = random_password.create_uppercase_letter_string()

    #analyze
    assert expected == actual

def test_lowercase_string():
    #setup
    expected = "abcdefghijklmnopqrstuvwxyz"

    #invoke
    actual = random_password.create_lowercase_letter_string()

    #analyze
    assert expected == actual

def test_digits_string():
    #setup
    expected = "0123456789"

    #invoke
    actual = random_password.create_digits_string()

    #analyze
    assert expected == actual

def test_symbols_string():
    #setup
    expected = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    #invoke
    actual = random_password.create_symbols_string()

    #analyze
    assert expected == actual
    
def test_rand_char_from_string_abc():
    #setup
    expected1 = "a"
    expected2 = "b"
    expected3 = "c"

    #invoke
    actual = random_password.get_random_char_from_string("abc")

    #analyze
    if actual == expected1:
        assert actual == expected1
    elif actual == expected2:
        assert actual == expected2
    elif actual == expected3:
        assert actual == expected3
    else:
        assert False