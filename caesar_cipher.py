# Caesar's Code - used by Caesar and the default shift
CAESARS_CODE = 3

def encrypt_letter(letter, shift = CAESARS_CODE):
    #im going to shift to the right
    #I will use chr and ord in order to convert to ascii and convert back 10 spaces to the ciphertext
    #I will return the encrypted ciphertext
    if(is_alphabetic(letter) == True):
        encrypted_value = ord(letter)
        encrypted_letter = chr(encrypted_value + shift)
        return encrypted_letter
    return ''

def encrypt_message(message, shift = CAESARS_CODE):
    ciphertext = ""
    values = range(0, len(message))
    for index in values:
        ciphertext = ciphertext + encrypt_letter(message[index], shift)
    return ciphertext


def decrypt_message(message, shift = CAESARS_CODE):
    text = ""
    for character in message:
        text = text + decrypt_letter(character, shift)
    return text

def decrypt_letter(letter, shift = CAESARS_CODE):
    #im going to decrypt my original encryption
    #by shifiting the same letters to the left, i will decrypt the message
    decrypted_value = ord(letter) - shift
    decrypted_letter = chr(decrypted_value)
    if(is_alphabetic(decrypted_letter) == True):
        return decrypted_letter
    return ''

def is_alphabetic(character):
    charValue = ord(character)
    if(charValue >= 65 and charValue <= 90):
        return True
    return False

def main():
    #letter = input("Enter a letter: ")
    #shift = int(input("Enter a shift: "))
    #print(encrypt_letter(letter, shift))
    #encrypted_letter = encrypt_letter(letter, shift)
    #print(decrypt_letter(encrypted_letter, shift))
    #is_alphabetic(letter)
    #message = input("Enter a 5 letter message: ")
    #print(encrypt_message(message, shift))

    phrase = input("enter a message with at least one space: ")
    words = phrase.split()
    for letters in words:
        print(encrypt_message(letters))

if __name__ == "__main__":
    main()