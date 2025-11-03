n,k = tuple(map(int,input().split()))

path = input()

def solution():
    curguess = "L" #0 = left
    curcrack = 0
    dead = 0
    while curcrack < len(path):
        if path[curcrack] != curguess:
            dead += 1
        else:
            if curguess == "L":
                curguess = "R"
            else:
                curguess = "L"
            
        if dead >= k:
            return 0
        curcrack += 1
    return k - dead

print(solution())
