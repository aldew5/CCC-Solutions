# This is the solution to problem 1 in CCC 2018
class Solution:
    def if_telemarketer(self, d1, d2, d3, d4):
        if d2 == d3:
            pass

            if d1 == '8' or d1 == '9' and d4 == '8' or d4 == '9':
                print("ignore")
            else:
                print("answer")
        else:
            print("answer")

d1 = input("> ")
d2 = input("> ")
d3 = input("> ")
d4 = input("> ")


# testing her out
person = Solution()
person.if_telemarketer(d1, d2, d3, d4)