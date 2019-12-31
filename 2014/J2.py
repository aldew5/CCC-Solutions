# Alec Dewulf
# J2 2014

num_votes = int(input())
votes = list(input())

a_votes = 0
b_votes = 0

x = 0
while x < num_votes:
    for v in votes:
        if v == 'A':
            a_votes += 1
        
        elif v == 'B':
            b_votes += 1
    x += 1

if b_votes < a_votes:
    print("A")
elif a_votes < b_votes:
    print("B")
else:
    print("Tie")
