arr = [[100.0,0],[0,100.0]]

for i in range(2,1000):
    pi = arr[i-1][0] + arr[i-2][0]
    tau = arr[i-1][1] + arr[i-2][1]
    tot = pi + tau
    arr.append([pi*100/tot,tau*100/tot])

n = int(input())

if n > 1000:
    print(round(arr[999][0],10),round(arr[999][1],10))
else:
    print(*arr[n-1])