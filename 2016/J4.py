# Alec Dewulf
# "Arrival Time" 2016 J4
# December 31, 2019
# Made it harder for myself by staying in hours. A better idea would be to use
# minutes and then convert back for the output.

d_time = list(input())
del d_time[2]

# converting to integers 
x = 0
while x < len(d_time):
    d_time[x] = int(d_time[x])

    x += 1
    
ten = [1, 0, 0, 0]
time = 0
add_time = 1

# Cycling through two hours of time
while time != 120:
    # Defining rush hour
    if d_time[1] >= 7 and d_time[1] <= 9 or d_time == ten:
        rush_hour = True
    else:
        rush_hour = False

    if rush_hour == True:
        add_time =  0.5
    else:
        add_time = 1
    # new minute
    if d_time[3] != 9 and d_time[1] != 4:
        d_time[3] += 1
        
    # new multiple of ten miinutes
    elif d_time[3] == 9 and d_time[2] != 5:
        d_time[3] = 0
        d_time[2] += 1
        
    # new one-digit hour
    elif d_time[3] == 9 and d_time[2] == 5 and d_time[1] != 9:
        d_time[1] += 1
        d_time[2] = 0
        d_time[3] = 0
        
    # switch to 10
    elif d_time[1] == 9 and d_time[2] == 5 and d_time[3] == 9:
        d_time[0] = 1
        d_time[1] = 0
        d_time[2] = 0
        d_time[3] = 0

    # new two-digit time
    elif d_time[2] == 5 and d_time[3] == 9 and d_time[0] == 1:
        # not to 20
        if d_time[1] != 9:
            d_time[1] +=1
        # to 20
        elif d_time[1] == 9:
            d_time[0] = 2
            d_time[1] = 0
            d_time[2] = 0
            d_time[3] = 0
    # to 00:01
    elif d_time[0] == 2 and d_time[1] == 4:
        d_time[0] = 0
        d_time[1] = 0
        d_time[2] = 0
        d_time[3] = 1
    time += add_time
        
print(d_time[0],d_time[1],':',d_time[2],d_time[3])
