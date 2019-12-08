# Alec Deuwlf
# Solution to CCC 2018 J3
# This was the hardest yet. Included comments to help explain

def solution():
    dis = input("> ")
    d = dis.split()

    # converting all the elements in d to integers
    for i in range(0,4):
        d[i] = int(d[i])

    # first element in first row of cities is 0
    cities = [0]

    # creates the first row stored in c
    for i in range(0,4):
         # adds distances to accumulating sums
         cities.append(cities[i] + d[i])

    # goes through all ins 0 - 5 for all ints 0-5
    for x in range(0,5):
        l = []
        for j in range(0,5):
            # when x = 0 the first row is formed...
            distance = cities[j] - cities[x]

            # so that there aren't negative values
            if distance < 0:
                distance *= -1
            
            l.append(distance)

        print(l)

# testing
solution()
