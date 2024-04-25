import calculator

def test_add_5_4():
    #setup
    x = 5
    y = 4
    expected = "5 + 4 = 9"

    #invoke
    actual = calculator.add(x, y)

    #analyze
    assert expected == actual

def test_subtract_5_4():
    #setup
    x = 5
    y = 4
    expected = "5 - 4 = 1"

    #invoke
    actual = calculator.subtract(x, y)

    #analyze
    assert expected == actual

def test_multiply_5_4():
    #setup
    x = 5
    y = 4
    expected = "5 * 4 = 20"

    #invoke
    actual = calculator.multiply(x, y)

    #analyze
    assert expected == actual

def test_divide_5_4():
    #setup
    x = 5
    y = 4
    expected = "5 / 4 = 1.25"

    #invoke
    actual = calculator.divide(x, y)

    #analyze
    assert expected == actual

def test_divide_5_0():
    #setup
    x = 5
    y = 0
    expected = "5 / 0 = NaN"

    #invoke
    actual = calculator.divide(x, y)

    #analyze
    assert expected == actual

def test_exponent_5_4():
    #setup
    x = 5
    y = 4
    expected = "5^4 = 625.0"

    #invoke
    actual = calculator.exponent(x, y)

    #analyze
    assert expected == actual