# Alec Dewulf
# "Are we there yet?" 2018 J3
# February 10, 2020

dist = input().split()

#convert to integers
x = 0
while x < len(dist):
    dist[x] = int(dist[x])

    x += 1

x = 0
lines = []
while x < len(dist) + 1:
    line = []
    num_before = x
    start = 0

    # forming the part of the line before 0
    while start < num_before:
        counter = 0
        s = 0
        for d in dist[start:num_before]:
            s += d
        line.append(s)
        start += 1

    # append the zero
    line.append(0)
    
    s = 0

    # formting the part of the line after 0
    for d in dist[x:]:
        line.append(s + d)
        s += d
    

    # convert in line into a string and print it
    ans = ''
    for n in line:
        ans += str(n)
        ans += ' '

    print(ans)
    x += 1
        
        

