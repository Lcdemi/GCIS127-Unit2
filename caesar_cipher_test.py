import caesar_cipher

def test_encrypt_shift_A_3():
    #setup
    letter = "A"
    shift = 3
    expected = "D"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_encrypt_shift_G_5():
    #setup
    letter = "G"
    shift = 5
    expected = "L"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_encrypt_shift_D_10():
    #setup
    letter = "D"
    shift = 10
    expected = "N"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_encrypt_shift_symbol():
    #setup
    letter = "#"
    shift = 1
    expected = ""

    #invoke
    actual = caesar_cipher.encrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_encrypt_shift_D():
    #setup
    letter = "D"
    expected = "G"

    #invoke
    actual = caesar_cipher.encrypt_letter(letter)

    #analyze
    assert expected == actual

def test_is_alphabetic_a():
    #setup
    letter = "a"
    expected = False
    
    #invoke
    actual = caesar_cipher.is_alphabetic(letter)

    #analyze
    assert expected == actual

def test_is_alphabetic_A():
    #setup
    letter = "A"
    expected = True
    
    #invoke
    actual = caesar_cipher.is_alphabetic(letter)

    #analyze
    assert expected == actual

def test_is_alphabetic_7():
    #setup
    letter = "7"
    expected = False
    
    #invoke
    actual = caesar_cipher.is_alphabetic(letter)

    #analyze
    assert expected == actual

def test_decrypt_shift_D_3():
    #setup
    letter = "D"
    shift = 3
    expected = "A"

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_decrypt_shift_L_5():
    #setup
    letter = "L"
    shift = 5
    expected = "G"

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_decrypt_shift_N_10():
    #setup
    letter = "N"
    shift = 10
    expected = "D"

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_decrypt_shift_symbol():
    #setup
    letter = "#"
    shift = 1
    expected = ""

    #invoke
    actual = caesar_cipher.decrypt_letter(letter, shift)

    #analyze
    assert expected == actual

def test_decrypt_shift_G():
    #setup
    letter = "G"
    expected = "D"

    #invoke
    actual = caesar_cipher.decrypt_letter(letter)

    #analyze
    assert expected == actual

def test_encrypt_message_HELLO_5():
    #setup
    message = "HELLO"
    shift = 5
    expected = "MJQQT"

    #invoke
    actual = caesar_cipher.encrypt_message(message, shift)

    #analyze
    assert expected == actual

def test_encrypt_message_HELLO_3():
    #setup
    message = "HELLO"
    shift = 3
    expected = "KHOOR"

    #invoke
    actual = caesar_cipher.encrypt_message(message, shift)

    #analyze
    assert expected == actual

def test_encrypt_message_HELLO():
    #setup
    message = "HELLO"
    expected = "KHOOR"

    #invoke
    actual = caesar_cipher.encrypt_message(message)

    #analyze
    assert expected == actual

def test_encrypt_message_ABC_2():
    #setup
    message = "ABC"
    shift = 2
    expected = "CDE"

    #invoke
    actual = caesar_cipher.encrypt_message(message, shift)

    #analyze
    assert expected == actual

def test_decrypt_message_MJQQT_5():
    #setup
    message = "MJQQT"
    shift = 5
    expected = "HELLO"

    #invoke
    actual = caesar_cipher.decrypt_message(message, shift)

    #analyze
    assert expected == actual

def test_decrypt_message_KHOOR_3():
    #setup
    message = "KHOOR"
    shift = 3
    expected = "HELLO"

    #invoke
    actual = caesar_cipher.decrypt_message(message, shift)

    #analyze
    assert expected == actual

def test_decrypt_message_KHOOR():
    #setup
    message = "KHOOR"
    expected = "HELLO"

    #invoke
    actual = caesar_cipher.decrypt_message(message)

    #analyze
    assert expected == actual