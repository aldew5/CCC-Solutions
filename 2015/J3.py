# "Rovarspraket" J3 2015
# Alec Dewulf
# January 4, 2020

"""
This problem took me an extremely high amount of code to solve mainly
because I don't know of a shortcut for writing repetitive if statements.
I'm new to problems like this so I'm going to look for ways of being more
efficient.
"""
name = input()

alph = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',\
            'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# finding the consonants in name
c_indices = []
vowels = []
for char in name:
    if char != 'a' and char != 'e' and char != 'i' and\
       char != 'o' and char != 'u':
        c_indices.append(alph.index(char))
    else:
        vowels.append(char)

n = 0
second_chars = []
# looping through all the indices of the cons. and finding the smallest
# difference between them and the next vowel
for i in c_indices:
    while i < len(alph):
        # checking to make sure dif is still an index of alph
        if i + n < len(alph):
            dif = i + n
            
        if alph[dif] == 'a' or alph[dif] == 'e' or alph[dif] == 'i'\
        or alph[dif] == 'o' or alph[dif] == 'u':
             sec = alph[dif]
             second_chars.append(sec)
             break
        # checking if there are i numbers to the left of n   
        if i - n >= 0:
            dif = i - n
            
        if alph[dif] == 'a' or alph[dif] == 'e' or alph[dif] == 'i'\
        or alph[dif] =='o' or alph[dif] == 'u':
            sec = alph[dif]
            second_chars.append(sec)
            break
        n += 1
            
third_chars = []
# finding the next closest vowel
for c in c_indices:
    i = 1
    while c + i < len(alph):
        if alph[c + i] != 'a' and alph[c + i] != 'e' and alph[c + i] != 'i'\
           and alph[c + i] != 'o' and alph[c + i] != 'u':
            third = alph[c + i]
            third_chars.append(third)
            break
        i += 1

groups = []
# forming the three character groups for each of the consonants
for i in range(0, len(c_indices)):
    group = alph[c_indices[i]] + second_chars[i] + third_chars[i]

    # adding the vowel if there still is one
    if len(vowels) > 0:
        group = group + vowels[0]
        vowels.pop(0)
    groups.append(group)
    
ans = ''
# printing the answer
for i in groups:
    ans = ans + i
print(ans)
     
