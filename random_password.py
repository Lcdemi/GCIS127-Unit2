import random #imports random class

def create_ascii_range_string(start, stop): #creates an ascii range string
    new_string = ""
    ascii_values = range(start, stop)
    for values in ascii_values:
        new_string += chr(values)
    return new_string

def create_uppercase_letter_string(): #creates a string with all uppercase letters
    uppercase_string = ""
    ascii_values = range(65, 91)
    for values in ascii_values:
        uppercase_string += chr(values)
    return uppercase_string

def create_lowercase_letter_string(): #creates a string with all lowercase letters
    lowercase_string = ""
    ascii_values = range(97, 123)
    for values in ascii_values:
        lowercase_string += chr(values)
    return lowercase_string

def create_digits_string(): #creates a string with all the digits
    digits_string = ""
    ascii_values = range(48, 58)
    for values in ascii_values:
        digits_string += chr(values)
    return digits_string


def create_symbols_string(): #creates a string with all special characters/symbols
    symbols_string = ""
    ascii_values = range(33, 48)
    for values in ascii_values:
        symbols_string += chr(values)
    ascii_values = range(58, 65)
    for values in ascii_values:
        symbols_string += chr(values)
    ascii_values = range(91, 97)
    for values in ascii_values:
        symbols_string += chr(values)
    ascii_values = range(123, 127)
    for values in ascii_values:
        symbols_string += chr(values)
    return symbols_string

def get_random_char_from_string(a_string): #grabs a random character from an inputted string
    random_int = random.randint(0, len(a_string) - 1)
    return a_string[random_int]

def generate_random_password(num_uppercase, num_lowercase, num_digits, num_symbols): #generates a random password
    password = ""
    num_uppercase = int(num_uppercase) #casting
    num_lowercase = int(num_lowercase)
    num_digits = int(num_digits)
    num_symbols = int(num_symbols)
    while num_digits + num_lowercase + num_symbols + num_uppercase > 0: #while more characters are still needed
        #print(num_uppercase) test code
        #print(num_lowercase)
        #print(num_digits)
        #print(num_symbols)
        choice = random.randint(1, 4) #random number between 1-4
        if choice == 1:
            if num_uppercase != 0:
                random_value = random.randint(0, 25)
                password += create_uppercase_letter_string()[random_value]
                num_uppercase -= 1
        elif choice == 2:
            if num_lowercase != 0:
                random_value = random.randint(0, 25)
                password += create_lowercase_letter_string()[random_value]
                num_lowercase -= 1
        elif choice == 3:
            if num_digits != 0:
                random_value = random.randint(0, 9)
                password += create_digits_string()[random_value]
                num_digits -= 1
        elif choice == 4:
            if num_symbols != 0:
                random_value = random.randint(0, 32)
                password += create_symbols_string()[random_value]
                num_symbols -= 1
    return password

def main():
    keep_going = True
    while keep_going == True: #loops until user exits
        nums = input("Enter <num uppers> <num lowers> <num digits> <num symbols>: ")
        individual_nums = nums.split(" ")
        if nums == "":
            print("Goodbye!")
            keep_going = False
        elif len(individual_nums) != 4:
            print("You must enter exactly 4 values")
        else:
            print("Password: " + generate_random_password(individual_nums[0], individual_nums[1], individual_nums[2], individual_nums[3]))

if __name__ == "__main__":
    main() #calls main
