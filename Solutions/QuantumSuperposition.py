from collections import deque
    
class Graph:
    class dirEdge:
        def __init__(self,origin,to,weight=1):
            self.to = to
            self.weight = weight
            self.origin = origin
    
    def __init__(self,n):
        self.adjarr = [[] for i in range(0,n)]
        self.size = n
        self.directed = False

    def printAdjList(self):
        for vertix in self.adjarr:
            printarr = []
            for edge in vertix:
                printarr.append((edge.to,edge.weight))
            print(printarr)
        
class DirectedGraph(Graph):
    def __init__(self,n):
        super().__init__(n)
        self.directed = True
    
    def insertDirectedEdge(self,vFrom,vTo,weight=1):
        self.adjarr[vFrom].append(Graph.dirEdge(vFrom,vTo,weight))
    
    def TopologicalSort(self):
        degreeList = [0 for _ in range(0,self.size)]
        zeroStack = deque()
        path = []

        for vertexlist in self.adjarr:
            for edge in vertexlist:
                degreeList[edge.to] += 1
        
        def addZeroNodes():
            for vertex in range(0, self.size):
                if degreeList[vertex] == 0:
                    zeroStack.append(vertex)

        addZeroNodes()
        while not len(zeroStack) == 0:
            curNode = zeroStack.popleft()
            path.append(curNode)
            for neighbour in self.adjarr[curNode]:
                degreeList[neighbour.to] -= 1
                if degreeList[neighbour.to] == 0:
                    zeroStack.append(neighbour.to)

        if len(path) == len(self.adjarr):
            return path
        else:
            return []

N1, N2, M1, M2 = tuple(map(int,input().split()))

G1 = DirectedGraph(N1)
G2 = DirectedGraph(N2)

for i in range(M1):
    origin, to = tuple(map(int,input().split()))
    origin -= 1
    to -= 1
    G1.insertDirectedEdge(origin,to)

for i in range(M2):
    origin, to = tuple(map(int,input().split()))
    origin -= 1
    to -= 1
    G2.insertDirectedEdge(origin,to)

Topo1 = G1.TopologicalSort()
Topo2 = G2.TopologicalSort()

dp1 = [[] for i in range(N1)]
dp2 = [[] for i in range(N2)]

dp1[0] = [0]
dp2[0] = [0]

for node in Topo1:
    for edge in G1.adjarr[node]:
        origin = edge.origin
        to = edge.to
        for steps in dp1[node]:
            if steps + 1 not in dp1[to]:
                dp1[to].append(steps + 1)

for node in Topo2:
    for edge in G2.adjarr[node]:
        origin = edge.origin
        to = edge.to
        for steps in dp2[node]:
            if steps + 1 not in dp2[to]:
                dp2[to].append(steps + 1)

dp1[-1].sort()
dp2[-1].sort()

def twosum(val):
    min = 0
    max = len(dp2[-1])-1
    while min < len(dp1[-1]) and max > -1:
        if dp1[-1][min] + dp2[-1][max] == val:
            return True
        elif dp1[-1][min] + dp2[-1][max] < val:
            min += 1
        elif dp1[-1][min] + dp2[-1][max] > val:
            max -= 1
    return False

Q = int(input())
Queries = [int(input()) for i in range(Q)]

for n in Queries:
    if not twosum(n):
        print("No")
    else:
        print("Yes")
