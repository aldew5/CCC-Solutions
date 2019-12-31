# Alec Dewulf
# "Double Dice" J3 2014
# December 21, 2019

num_rounds = int(input())

a = 100
d = 100

x = 0
while x < num_rounds:
    points = input().split()
    if points[0] > points[1]:
        d -= int(points[0])
    elif points[1]> points[0]:
        a -= int(points[1])

    x += 1

print(a)
print(d)

