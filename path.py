from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

#Parsing
N, M, K = tuple(map(int,input().split(" ")))
colors = list(map(int,input().split(" ")))

#Zero index the colours
for i in range(0,N):
    colors[i] -= 1

adj = defaultdict(list)

#Build adjacency List and zero index it
for i in range(0,M):
    edge = tuple(map(int,input().split(" ")))
    adj[edge[0]-1].append(edge[1]-1)
    adj[edge[1]-1].append(edge[0]-1)

#Group vertices by color
colourNodes = [[] for _ in range(0,K)]
for u in range(0, N):
    colourNodes[colors[u]].append(u)

#Setup memoisation
maxM = 2**(K)
dp = [[0]*maxM for i in range(0,N)]

#Precompute all valid colour paths
maskColours = [
    [c for c in range(K) if (m & (1<<c))]
    for m in range(maxM)]

#These are all the possible colour paths, sorted in decreasing order (to have full masks first)
masks = list(range(maxM))
masks.sort(key=lambda x: bin(x).count("1"), reverse=True)

for mask in masks:
    #Loop over all colours
    for color in maskColours[mask]:
        for u in colourNodes[color]:
            total = 0
            #Check all adjacent nodes
            for v in adj[u]:
                nextColour = colors[v]
                #Only do this if the colour hasn't been used yet
                if not (mask & (1 << nextColour)):
                    new_mask = mask | (1 << nextColour)
                    #Current path + all possible paths from before
                    total += 1 + dp[v][new_mask]
            #Update the memoisation
            dp[u][mask] = total

answer = sum(dp[u][ 1 << colors[u]] for u in range(0, N))
print(answer)