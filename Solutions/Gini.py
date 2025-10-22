n = int(input())

y = [int(input()) for _ in range(0,n)]

y.sort()

diffarr = [y[i+1] - y[i] for i in range(0,n-1)]

nominator,denominator = (0,0)

for i in range(1,n):
    nominator += 2*(n-i)*i*diffarr[i-1]

for i in range(0,n):
    denominator += 2*y[i]*n

print(nominator/denominator)
