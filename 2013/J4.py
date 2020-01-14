# "Time on Task" J4 2013
# Alec Dewulf
# January 14, 2020

time = int(input())
num_chores = int(input())

chores = []
x = 0
# get all the different times for the chores
while x < num_chores:
    chore = int(input())
    chores.append(chore)

    x += 1


time_spent = 0
completed_chores = 0

# add the next shortest chore to the time spent
# until time_spent exceeds time.
# equal is included in the case of a 0 minute chore
while time_spent <= time:
    # add the shortest chore
    time_spent += min(chores)

    # take it off the list and add a completed chore
    chores.pop(chores.index(min(chores)))
    completed_chores += 1

# if there wasn't a 0 minute chore and it went over time
# subtract a chore.
if time_spent > time:
    completed_chores -= 1
    
print(completed_chores)
