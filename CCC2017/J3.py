# "Exactly Electrical" J3 2017
# Alec Dewulf
# December 26, 2019

starting_coords = input().split()
dest_coords = input().split()
charge = int(input())

# convert the items into integers
x = 0
while x < len(starting_coords):
    starting_coords[x] = int(starting_coords[x])
    x += 1
    
x = 0
while x < len(dest_coords):
    dest_coords[x] = int(dest_coords[x])
    x += 1

# the distance between them is the distance between y and x
d_between = abs(starting_coords[0] - dest_coords[0]) + abs(starting_coords[1] - dest_coords[1])


# when their difference is divisible by 2 you can go back and forth
# to land on the answer
if (charge - d_between) % 2 == 0:
    print("Y")
else:
    print("N")
