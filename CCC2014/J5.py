
# Alec Dewulf
# "Assigning Partners" J5 2014
# This one was surprisingly much easier than J4
# December 21, 2019

num_students = int(input())

group_1 = input().split()
group_2 = input().split()

good = 0
bad = 0

x = 0
while x < num_students:
    if group_1[x] == group_2[x]:
        bad += 1
        break
    elif group_1[x] != group_2[x]:
        good += 1
        x += 1
    

if good == num_students:
    print("good")
else:
    print("bad")

        
