# Alec Dewulf
# 2018 J1 "Occupy Parking"
# February 10, 2020

num_spots = int(input())
today = list(input())
yesterday = list(input())

num_occupied = 0
x = 0
while x < num_spots:
    if today[x] == yesterday[x] and today[x] == 'C':
        num_occupied += 1

    x += 1

print(num_occupied)
