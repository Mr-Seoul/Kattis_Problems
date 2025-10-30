import math
n = int(input())

def floor100(num):
    return str(round(math.floor(100*num+1/(1e6))/100,2))

def approx(a,b):
    if abs(a-b) < 1/1e6:
        return True
    else:
        return False

def valid(num):
    tdf = 0.015
    whole = num // tdf
    nextwhole = whole + 1

    if floor100(whole*tdf)==floor100(num) or floor100(nextwhole*tdf)==floor100(num):
        return "VALID"
    else:
        return "IMPOSSIBLE"

for _ in range(n):
    t = float(input())
    print(valid(t))