# Alec Dewulf
# "Assigning Partners" J5 2014

num_students = int(input())
n1 = input().split()
n2 = input().split()

# initialize variables
x, num_bad = 0, 0
# loop through all students in one list
while x < num_students:
    y = 0
    # for each of those students loop through the students in the other list
    while y < num_students:
        # the pair is the first instance of a particular child
        # and his/her partner
        pair = [n1[x], n2[x]]

        # kid is partnered with him/herself
        if pair[0] == pair[1]:
            num_bad += 1
            break

        # if the first child comes up again and their partner is different
        if n1[y] in pair and n2[y] not in pair:
            num_bad += 1
            break
        # the second child had a different partner
        elif n2[y] in pair and n1[y] not in pair:
            num_bad += 1
            break
        y += 1

    # if there was a mistake leave the outer loop
    if num_bad == 1:
        break
    else:
        x += 1

# output results
if num_bad == 1:
    print('bad')
else:
    print('good')
