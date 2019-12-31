# Alec Dewulf
# "Magic Squares" 2016 J2
# December 30, 2019

l1 = input().split()
l2 = input().split()
l3 = input().split()
l4 = input().split()

# converting indices to integers
x = 0
while x < len(l1):
    l1[x] = int(l1[x])
    l2[x] = int(l2[x])
    l3[x] = int(l3[x])
    l4[x] = int(l4[x])
    x += 1

# finding the sums of the rows
s = 0
lines = []
for num in l1:
    s += num
lines.append(s)
s = 0
for num in l2:
    s += num
lines.append(s)
s = 0
for num in l3:
    s += num
lines.append(s)
s = 0
for num in l4:
    s += num
lines.append(s)

# checking for a non-magic square
wrong = 0
if lines[0] != lines[1] or lines[2] != lines[3]:
    wrong += 1

# checking the columns
y = 0
while y < len(l1) -1:
    row = l1[y] + l2[y] + l3[y] + l4[y]

    if row != lines[0]:
        wrong +=1
    y += 1

# returning output
if wrong == 0:
    print("magic")
else:
    print("not magic")




    
