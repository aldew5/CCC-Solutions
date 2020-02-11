# Alec Dewulf
# "Hidden Palindrome" 2016 J3
# December 31, 2019

pal = input()
lengths = []

x = 1
y = 1
# getting lengths of palindromes that have a middle consisting of 1 letter
while x < len(pal) - 1:
    # checking to make sure the guess is whithin the length of the palindrome
    while (x + y) < len(pal) and (x - y) >= 0:
        if pal[x - y] == pal[x + y]:
            # multiply ans by two for the letters on both sides and
            # add the middle
            ans = (2 * y) + 1
            lengths.append(ans)
            y += 1
        else:
            break
    y = 1
    x += 1
    
y = 1
x = 1
# getting the lengths of palindromes that have a middle of 2 letters
while x < len(pal) - 1:
        # checking for a two letter middle
        if pal[x] == pal[x + 1]:
            y = 1
            # finding the largest palindrome
            while (x + 1 + y) < len(pal):
                # the digits after the two digit middle are the same
                if pal[x - y] == pal[x + y + 1] and (x-y) >= 0:
                    ans = (2 * y) + 2
                    lengths.append(ans)
                    y +=1
                else:
                    break
        x += 1

# returning the answer which is the greatest length found
if len(lengths) != 0:
    print(max(lengths))
else:
    print(1)


