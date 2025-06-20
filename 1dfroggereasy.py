def algo(n,s,m,steps):
    visitedTiles = []
    visitedTiles.append(s)
    turns = 0
    if steps[s-1] == m:
        return ("magic",turns)
    while True:
        s += steps[s-1]
        turns += 1
        if s not in visitedTiles:
            visitedTiles.append(s)
            if s < 1:
                return("left",turns)
            elif s > n:
                return("right",turns)
            elif steps[s-1] == m:
                return ("magic",turns)
            
        else:
            return ("cycle",turns)
            
#--------------------------------------#

n, s ,m  = map(int,input().split(" "))

steps = input().split(" ")
steps = [int(step) for step in steps]

results = algo(n,s,m,steps)
print(results[0])
print(results[1])