# Alec Dewulf
# "Tournament Selection" 2016 J1
# December 30, 2019

games = []

x = 0
while x < 6:
    games.append(input())

    x +=1

num_wins = 0

for g in games:
    if g == "W":
        num_wins += 1

if num_wins == 0:
    print(-1)
elif num_wins == 1 or num_wins == 2:
    print(3)
elif num_wins == 3 or num_wins == 4:
    print(2)
elif num_wins == 5 or num_wins == 6:
    print(1)
