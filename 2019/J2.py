# Alec Dewulf
# "Time to Decompress" J2 2019

num_lines = int(input())
all_messages = []

x = 0
# get input for the number of lines create the message
# then append it
while x < num_lines:
    line = input().split()
    message = int(line[0]) * line[1]
    all_messages.append(message)

    x += 1

# print the messages
for x in all_messages:
    print(x)

