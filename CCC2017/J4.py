# "Favourite Times" J4 2017
# Alec Dewulf
# December 26, 2019
# An extremely long problem that requires you to literlly make a clock

duration = int(input())

# starting time is 12: 00
time = [1, 2, 0, 0]

y = 0
num_sequence = 0

while y < duration:
    # FOUR DIGIT TIME
    if len(time) == 4:
        # not a new multiple of ten minutes in 4 digit time
        if time[3] != 9:
            new_min = time[3] + 1
            time.pop(3)
            time.append(new_min)

    # is a new multiple of ten minutes in 4 digit time
        elif time[3] == 9 and time[2] != 5:
            time.pop(3)
            new_min = time[2] + 1
            time.pop(2)
            time.append(new_min)
            time.append(0)

    # for 12:59         
        elif sum(time) == 17:
            time = [1, 0, 0]

    # normal hour for 4 digits
        elif time[2] == 5 and time[3] == 9:
            new_hour = time[1] + 1
            time = [1, new_hour, 0, 0]

    # 12:34 is an arithamtic sequence
    if len(time) == 4:
       if time[1] == 2 and time[2] == 3 and time[3] ==4:
            num_sequence += 1
            

    # THREE DIGIT TIME
    elif len(time) == 3:
        # three digit time new minute
        if time[2] != 9:
            new_min = time[2] + 1
            time.pop(2)
            time.append(new_min)
    # 100
    # three digit time new multiple of 10 minutes
        elif time[2] == 9 and time[1] != 5:
            new_min = time[1] + 1
            time.pop(2)
            time.pop(1)
            time.append(new_min)
            time.append(0)
        # adding a new normal hour
        elif time[2] == 9 and time[1] == 5 and time [0] != 9:
            new_hour = time[0] + 1
            time = [new_hour, 0, 0]
        # going from 9:59 to 10:00
        elif time[0] == 9 and time[1] == 5 and time[2] == 9:
            time = [1, 0, 0, 0]

        # checking for an arithmatic sequence
        for i in range(0, 5):
            if time[0] + i == time[1] and time[1] + i == time[2]:
                num_sequence += 1
            elif time[0] - i == time[1] and time[1] - i == time[2]:
                num_sequence += 1

    y += 1
    

print(num_sequence)       
        
