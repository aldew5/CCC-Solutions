# My solution for CCC J12019
a_3 = int(input("> "))
a_2 = int(input("> "))
a_1 = int(input("> "))
b_3 = int(input("> "))
b_2 = int(input("> "))
b_1 = int(input("> "))

def solution():
    a3 = a_3 * 3
    a2 = a_2 * 2

    a_total = a2 + a3 + a_1

    b3 = b_3 * 3
    b2 = b_2 * 2

    b_total = b3 + b2 + b_1

    if b_total < a_total:
        print("A")
    elif a_total < b_total:
        print("B")
    else:
        print("T")

solution()
