def add(x, y):
    sum = x + y
    function = str(x) + " + " + str(y) + " = " + str(sum)
    return function

def subtract(x, y):
    difference = x - y
    function = str(x) + " - " + str(y) + " = " + str(difference)
    return function

def multiply(x, y):
    product = x * y
    function = str(x) + " * " + str(y) + " = " + str(product)
    return function

def divide(x, y):
    if(y == 0):
        function = str(x) + " / " + str(y) + " = " + "NaN"
        return function
    quotient = x / y
    function = str(x) + " / " + str(y) + " = " + str(quotient)
    return function

def exponent(x, y):
    power = float(x**y)
    function = str(x) + "^" + str(y) + " = " + str(power)
    return function

def main():
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    print(exponent(x, y))
main()