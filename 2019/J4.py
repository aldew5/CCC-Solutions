# Alec Dewulf
# "Flipper" J4 2019

flips = input()

# the grid
line1 = (1, 2)
line2 = (3, 4)

# defining variables
num_hor = 0
num_vert = 0

# finding number of vertical and horizontal flips
for f in flips:
    if f == "H":
        num_hor += 1
    else:
        num_vert += 1

# horizontal flip
x = 0
while x < num_hor:
    # line 1
    for n in line2:
        if n == line2[0]:
            pos1 = n
        else:
            pos2 = n

    for n in line1:
        if n == line1[0]:
            pos3 = n
        else:
            pos4 = n
            
    line1 = (pos1, pos2)
    line2 = (pos3, pos4)

    x += 1

# vertical flip
x = 0
while x < num_vert:
    for n in line1:
        if n == line1[0]:
            pos2 = n
        else:
            pos1 = n
            
    for n in line2:
        if n == line2[0]:
            pos4 = n
        else:
            pos3 = n

    line1 = (pos1, pos2)
    line2 = (pos3, pos4)

    x += 1


# output results
print(line1[0], line1[1])
print(line2[0], line2[1])
