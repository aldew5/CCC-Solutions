# Alec Dewulf
# "Tandem Bicycle" J5 2016
# February 11, 2020

question = int(input())
num_people = int(input())
dmoj_v = input().split()
peg_v = input().split()

# convert lists to ints
for s in range(len(dmoj_v)):
    dmoj_v[s] = int(dmoj_v[s])

for s in range(len(peg_v)):
    peg_v[s] = int(peg_v[s])

# problem one
if question == 1:
    x, total_speed = 0, 0
    while x < num_people:
        speeds = [max(dmoj_v), max(peg_v)]
        bike_speed = max(speeds)

        # take used up speeds off of the list
        dmoj_v.pop(dmoj_v.index(max(dmoj_v)))
        peg_v.pop(peg_v.index(max(peg_v)))

        # add to total speed and reset bike speed
        total_speed += bike_speed
        bike_speed = 0

        x += 1

elif question == 2:
    x, total_speed = 0,0
    while x < num_people:
        speeds = [max(dmoj_v), min(peg_v)]
        bike_speed = max(speeds)

        dmoj_v.pop(dmoj_v.index(max(dmoj_v)))
        peg_v.pop(peg_v.index(min(peg_v)))

        total_speed += bike_speed
        bike_speed = 0

        x += 1

# output results
print(total_speed)
