# "Happy or Sad" J2 2015
# Alec Dewulf
# January 4, 2020


"""
This problem appears easy until you consider faces may appear in the
same index.  The solution is to split up the indices with
faces(removoing the colon) so that if they were part of the same index
they aren't anymore and can be counted properly

"""

message = input().split()

num_happy = 0
num_sad = 0
for c in message:
    if ':-)' in c:
        happy_list = c.split(':')
        
        for h in happy_list:
            if '-)' in h:
                num_happy += 1
                
    elif ':-(' in c:
        sad_list = c.split(":")
        
        for s in sad_list:
            if '-(' in s:
                num_sad += 1

print(num_happy, num_sad)
        
