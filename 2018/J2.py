# This is my solution to CCC 2018 problem #2
class Solution:
    def check_cars(self, length, string1, string2):
        # splitting the strings into lists
        list1 = list(string1)
        list2 = list(string2)

        x = 0
        y = 0
        while x < length:
            if list2[x] == list1[x] and list1[x] == 'C' and list2[x] == 'C':
                y += 1
            x += 1
        print(y)

length = int(input("> "))
string1 = input("> ")
string2 = input("> ")

# testing it out
day = Solution()
day.check_cars(length, string1, string2)
