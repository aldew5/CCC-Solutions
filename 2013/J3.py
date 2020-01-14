# "From 1987 to 2013" J3 2013
# Alec Dewulf
# January 14, 2019

year = int(input())

numbers = []
double_num = 0

# infinite loop
while True:
    year += 1
    year = str(year)

    # append to a list of new ints or mark it as a double
    for i in year:
        if i not in numbers:
            numbers.append(i)
        elif i in numbers:
            double_num += 1

    if double_num == 0:
        # this is a perfect year
        break
    else:
        # reset the variables
        numbers = []
        double_num = 0
        # so year can be added onto
        year = int(year)

    
# output results
print(year)
    
