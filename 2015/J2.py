# "Happy or Sad" J2 2015
# Alec Dewulf
# January 4, 2020


message = input().split()

num_happy = 0
num_sad = 0
clean_message = []

# separating each face into a separate index
for c in message:
    clean = c.split(':')

    sent = ' '
    # create a string of the elements of clean
    for i in clean:
        sent += i

    # check the string for a happy or sad face
    if '-)' in sent:
        num_happy += 1
    elif '-(' in sent:
        num_sad += 1
        
    
        
# outputs
if num_happy == 0 and num_sad == 0:
    print('none')
elif num_happy == num_sad:
    print('unsure')
elif num_happy > num_sad:
    print("happy")
elif num_happy < num_sad:
    print('sad')
