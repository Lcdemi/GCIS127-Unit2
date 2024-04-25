def boolean_expressions(a, b, c):
    print("a =", a, "b =", b, "c =", c)
    print("a is greater than b:", (a > b))
    print("b is equal to c:", (b == c))
    print("a is less than or equal to c:", (a <= c))
    print("a is not equal to c:", (a != c))
    print("a is greater than b and c:", (a > b and a > c))
    print("b is less than c or a is less than b:", (b < c or a < b))

def main():
    boolean_expressions(10, 5, 15)
    boolean_expressions(1, 2, 3)
    boolean_expressions(15, 10, 5)

main()