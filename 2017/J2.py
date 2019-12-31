# "Shifty Sum" J2 2017
# Alec Dewulf

num = int(input())
num_shifts = int(input())

shifty_sum = num

x = 0
while x < num_shifts:
    num *= 10
    shifty_sum += num

    x += 1

    
print(shifty_sum)
