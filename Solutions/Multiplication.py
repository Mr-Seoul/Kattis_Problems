result, N = (1,int(input()))

for i in range(N):
    result *= int(input())

print(result % (10**9 + 1))
