# "Special Day" J1 2015
# Alec Dewulf
# January 4, 2020

month = int(input())
day = int(input())

if month < 2 or month == 2 and day < 18:
    print("Before")
elif month > 3 or month == 2 and day > 18:
    print("After")
elif month == 2 and day == 18:
    print("Special")
