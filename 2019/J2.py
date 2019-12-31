# Alec Dewulf
# Solution to CCC  2019 J2

length = int(input("> "))
message = []

x = 0
while x < length:
    symbol = input("> ").split()
    multiple = int(symbol[0])
    row = symbol[1] * multiple
    message.append(row)

    x += 1

y = 0
while y < length:
    print(message[y])
    y += 1
