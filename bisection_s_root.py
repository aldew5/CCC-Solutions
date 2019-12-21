# Alec Dewulf
# Bisection search to find root

def find_root(num, epsilon):
    low = 0
    high = num
    ans = (high + low)/2.0

    while abs(ans**2 - num) >= epsilon:
        if ans**2 < num:
            low = ans
        elif ans**2 > num:
            high= ans

        ans = (high + low)/2.0

    return ans

print(find_root(25, 0.001))
