# Alec Dewulf
# 2018 J1 "Telemarketer or not?"
# February 10, 2020

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if n1 == 8 or n1 == 9:
    if n4 == 8 or n4 == 9:
        if n3 == n2:
            print('ignore')
        else:
            print('answer')
    else:
        print('answer')
else:
    print('answer')
