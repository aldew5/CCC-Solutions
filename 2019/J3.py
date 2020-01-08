# Alec Dewulf
# "Cold Compress" J3 2019


num_lines = int(input())

# define variables
rows = []
counter = 0
row = ''

x = 0
# get new lines until they've all been compressed
while x < num_lines:
    line = input()
    y = 0
    row = ''

    # loop through the line
    while y < len(line):
        # if there is no index after line[y] add the new symbol and append
        if y + 1 == len(line):
            counter += 1
            row += str(counter) + ' ' + line[y] + ' '
            rows.append(row)

            counter = 0
            y += 1

        # if the next thing is different add the previous data
        # onto the row
        elif line[y] != line[y + 1]:
            counter += 1
            row += str(counter) + ' ' + line[y] + ' ' 
            
            counter = 0
            y += 1

        # if the next symbol is the same continue 
        elif line[y] == line[y + 1]:
            counter += 1
            y += 1
    x += 1

# print out results
for r in rows:
    print(r)
