def convert_height():
    height = input("Please enter your height in inches: ")
    inches = int(height) % 12
    feet = int(height) // 12
    print("You are ", feet, "' ", inches, "\""," tall", sep="")

def before(letter):
    ascii_code = ord(letter)
    character1 = chr(ascii_code)
    character2 = chr(ascii_code - 1)
    character3 = chr(ascii_code - 2)
    character4 = chr(ascii_code - 3)
    print(character1)
    print(character2)
    print(character3)
    print(character4)

def main():
    convert_height()
    before("D")

main()