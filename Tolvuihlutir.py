import heapq

#Parsing
n, k, p = tuple(map(int, input().split(" ")))

parts = input().split(" ")

PartsList = {}

for i in parts:
    PartsList.update({i:[]})

for i in range(0,n):
    line = input().split(" ")
    PartsList[line[0]].append((int(line[1]),int(line[2])))

#Eliminate parts that are more expensive, but less performant
for part in PartsList.keys():
    #Sort based on price
    PartsList[part].sort(key=lambda x: (x[0], -1*x[1]))

    #Keep cheapest item
    newList = []
    lastPerformance = -1

    #Only keep item if it is more performant than the last, cheaper item
    for curPart in PartsList[part]:
        if curPart[1] > lastPerformance:
            lastPerformance = curPart[1]
            newList.append(curPart)
    
    #Update list
    PartsList[part] = newList

heaps = [[] for i in range(0,k)]

curParts = [(0,-1) for i in range(0,k)]
totPrice = 0
exhausted = [False for i in range(0,k)]

weakestHeap = [(-1,i) for i in range(0,k)]

#Add all parts to heaps
for partIndex in range(0,len(parts)):
    for part in PartsList[parts[partIndex]]:
        heapq.heappush(heaps[partIndex],part)

valid = True

#Setup exhausted list
for i in range(0,len(parts)):
    if len(heaps[i]) == 0:
        valid = False

def totalPerformance():
    minPerf = float('inf')
    for i in range(0,len(curParts)):
        if curParts[i][1] < minPerf:
            minPerf = curParts[i][1]

    return minPerf

while totPrice <= p and valid:
    #If no more parts are available, go to finish
    if len(weakestHeap) == 0:
        break
    
    #Get current state of performance and the weakest Link
    perf, weakestLink = heapq.heappop(weakestHeap)

    #Get newest upgrade
    newPart = heapq.heappop(heaps[weakestLink])


    #Keep track of exhausted parts. If no other parts are available, don't readd the old part
    if len(heaps[weakestLink]) != 0:
        heapq.heappush(weakestHeap, (newPart[1], weakestLink))
    
    #Update price
    totPrice += newPart[0] - curParts[weakestLink][0]
    
    #Break once the price gets too high, go to finish. Otherwise add the new part
    if totPrice > p:
        break
    else:
        curParts[weakestLink] = newPart

#Final Evaluation
finalPerformance = totalPerformance()

if finalPerformance == -1:
    print("O nei!")
else:
    print(finalPerformance)