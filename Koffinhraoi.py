import heapq

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
ranges.sort(key=lambda x: (x[1],-1*x[0]))  

time = 0
coffees = 0
durationsHeap = [] # 

for duration, deadline in ranges:
    heapq.heappush(durationsHeap, -1*duration)
    time += duration

    while time > deadline:
        maxDuration = -1*heapq.heappop(durationsHeap)
        newDuration = maxDuration // 2

        timeSaved = (maxDuration - newDuration)
        time -= timeSaved
        
        heapq.heappush(durationsHeap, -1*newDuration)
        coffees += 1

print(coffees)
