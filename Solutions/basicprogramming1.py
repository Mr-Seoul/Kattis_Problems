N, t = tuple(map(int,input().split()))
A = tuple(map(int,input().split()))

def return7():
    return 7

def equalitytest():
    if A[0]>A[1]:
        return "Bigger"
    elif A[0]==A[1]:
        return "Equal"
    else:
        return "Smaller"

def median():
    return sorted(A[0:3])[1]

def sumA():
    tot = 0
    for num in A:
        tot += num
    return tot

    
def sumevenA():
    tot = 0
    for num in A:
        if num % 2 == 0:
            tot += num
    return tot

def lettermapping():
    letters = "abcdefghijklmnopqrstuvwxzy"
    map = [" " for i in range(N)]
    for i in range(N):
        map[i] = letters[A[i]%26]
    return "".join(map)

def indexjumping():
    visited = bytearray(N)
    index = 0
    while True:
        if index == N - 1:
            return "Done"
        if index < 0 or index >= N:
            return "Out"
        if visited[index]:
            return "Cyclic"
        visited[index] = 1
        index = A[index]
        
if t == 1:
    print(return7())
elif t==2:
    print(equalitytest())
elif t == 3:
    print(median())
elif t == 4:
    print(sumA())
elif t == 5:
    print(sumevenA())
elif t == 6:
    print(lettermapping())
elif t == 7:
    print(indexjumping())
