# Alec Dewulf
# "Winning Score" J1 2019
# January 8, 2020

a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

apples_points = (a3 * 3) + (a2 * 2) + a1
bananas_points = (b3 * 3) + (b2 * 2) + b1

if apples_points > bananas_points:
    print("A")
elif bananas_points > apples_points:
    print("B")
