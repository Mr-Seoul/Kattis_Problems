s = (int(i) for i in input().split(" "))
e = (int(i) for i in input().split(" "))
p = (int(i) for i in input().split(" "))

s = list(s)
e = list(e)
p = list(p)

long = 1000000

dirS = [s[0]-p[0],s[1]-p[1]]

dirE = [e[0]-p[0],e[1]-p[1]]

def normalize(vec):
    return [0 if vec[0] == 0 else int(vec[0]/abs(vec[0])),0 if vec[1] == 0 else int(vec[1]/abs(vec[1]))]

dirS = normalize(dirS)
dirE = normalize(dirE)

differingNorms = 0

if dirS[0] != dirE[0]: differingNorms += 1
if dirS[1] != dirE[1]: differingNorms += 1

#First to wall, then to corner, then potentially to other corner, then potentially to new access point, then to end
path = []
path.append([dirS[0], dirS[1]])
curPoint = dirS
Finished = False
while not Finished:
    if curPoint[0] != 0 and curPoint[1] != 0:

        if curPoint[0] != dirE[0] and curPoint[1] != dirE[1]: #Not same Edge
            if curPoint[0] == -1 and curPoint[1]  == -1: #Bottom Left
                path.append([-1,1])
                curPoint = [-1,1]
            elif curPoint[0] == -1 and curPoint[1] == 1: #Top Left
                path.append([1,1])
                curPoint = [1,1]
            elif curPoint[0] == 1 and curPoint[1] == 1: #Top Right
                path.append([1,-1])
                curPoint = [1,-1]
            elif curPoint[0] == 1 and curPoint[1] == -1: #Bottom Right
                path.append([-1,-1])
                curPoint = [-1,-1]
        else:
            path.append(dirE)
            print(len(path)+1)
            for i in path:
                print(i[0]*long, i[1]*long)
            print(e[0],e[1])
            Finished = True
    else:
        if curPoint[0] == 0 and curPoint[1] > 0: #Center top
            curPoint = [1, curPoint[1]]
            path.append(curPoint)
            
        elif curPoint[0] == 0 and curPoint[1] < 0: #Center bottom
            curPoint = [-1, curPoint[1]]
            path.append(curPoint)
            
        elif curPoint[0] > 0 and curPoint[1] == 0: #Center right
            curPoint = [curPoint[0], -1]
            path.append(curPoint)
            
        elif curPoint[0] < 0 and curPoint[1] == 0: #Center left
            curPoint = [curPoint[0], 1]
            path.append(curPoint)