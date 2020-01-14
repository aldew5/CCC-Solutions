# "Rotating Letter" J2 2014
# Alec Dewulf
# January 12, 2020

message = input()

special_letters = ['I', 'O','S', 'H', 'Z', 'X', 'N']

num_wrong = 0
for l in message:
    if l not in special_letters:
        num_wrong += 1

if num_wrong == 0:
    print("YES")
else:
    print("NO")
