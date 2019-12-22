# Alec Dewulf
# "Party Invitation" 2014 J4
# This one was kinda difficult and I probably solved it really inefficiently
# December 21, 2019

num_friends = int(input())
rounds = int(input())

# function to remove the duplicates in the list
def remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

friends_l = []

# give the friends numbers
for i in range(1, num_friends + 1):
    friends_l.append(i)

m = []
x = 0

# getting user input for the intervals to take out stored in m
while x < rounds:
    m.append(int(input()))

    x += 1

y = 0
index = -1
correct = []

# find the correct indices for each of the intervals in m index starts at -1
# because the index of a list starts at 0
for i in m:
    while index <= len(friends_l):
        index += i
        correct.append(index)

        if correct[-1] > len(friends_l)- 1:
            correct.pop(-1)
            
    # remove the duplicates and reverse the list so it doesn't mess with the
    # indices
    answer = remove(correct)
    answer.sort(reverse=True)

    # delete the correct values
    for values in answer:
        del friends_l[values]

    # reset the index and clear correct
    index = -1
    correct.clear()


# printing the answer
for i in friends_l:
    print(i)
