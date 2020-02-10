# Alec Dewulf
# "Sunflowers" J4 2018
# February 10, 2020

num_flowers = int(input())

x, rows = 0, []
while x < num_flowers:
    row = input().split()

    # converting list items to ints
    y = 0
    while y < len(row):
        row[y] = int(row[y])
        y += 1
        
    rows.append(row)
    x += 1


def rotate_right(rows):
    x, new_rows = 0, []
    while x < num_flowers:
        l = []
        for r in reversed(rows):
            l.append(r[x])
            
        new_rows.append(l)

        x += 1
    return new_rows

def rotate_left(rows):
    x, new_rows = len(rows) - 1, []
    while x >= 0:
        l = []
        for r in rows:
            l.append(r[x])

        new_rows.append(l)

        x -=1
    return new_rows


counter = 0
while True:
    num_correct = 0

    # if no rotations are required
    if counter == 0:
        for r in rows:
            if sorted(r) == r:
                num_correct += 1
        l = []
        # make a list of the first elements in each row
        for n in rows:
            l.append(n[0])

        # all rows are in ascending order and the first elements are in order
        if num_correct == num_flowers  and sorted(l) == l:
            chart = rows
            break
        else:
            num_correct = 0

    # a left rotation is required             
    chart = rotate_left(rows)
    for r in chart:
        if sorted(r) == r:
            num_correct += 1

    l = []
    for n in chart:
        l.append(n[0])

    # all the rows were in anscending order
    if num_correct == num_flowers and sorted(l) == l:
        break
    else:
        num_correct = 0

    # a right rotation is required
    chart = rotate_right(rows)
    for r in chart:
        if sorted(r) == r:
            num_correct += 1

    l = []
    for n in chart:
        l.append(n[0])


    if num_correct == num_flowers  and sorted(l) == l:
        break
    else:
        num_correct = 0
        rows = rotate_right(rows)

    counter += 1

# print out the rows in the chart as strings
for r in chart:
    ans = ''
    for n in r:
        ans += str(n)
        ans += ' '

    print(ans)
