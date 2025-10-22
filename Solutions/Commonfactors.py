import math
n = int(input())

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

#Find maximum value of factorial to use as base
factorindex = 0
curnum = 1
while curnum <= n:
    curnum *= primes[factorindex]
    factorindex += 1

#Return to previous value inside
factorindex -= 1
curnum = curnum//primes[factorindex]

#Can do time complexity 2^n
#Inclusion exclusion, do dp and then add up every with uneven used numbers and subtract all with even used numbers

#Idea, use bitmaps and do old = new |= ~(1 << n)

dp = [0 for _ in range(0,pow(2,factorindex))]

#The amount of ways to divide n is 1
dp[-1] = 1

sum = 0

#1 is used, 0 is unused
for index in range(len(dp)-1,-1,-1):
    def count1s(num):
        result = 0
        for i in range(factorindex):
            if (num & (1 << i) > 0):
                result += 1
        return result

    #Multiply each prime where the bitset is 0
    def extractfactor(num):
        factor = 1
        for i in range(factorindex):
            if num & (1 << i) > 0:
                factor *= primes[i]
                
        return factor
    
    dp[index] = curnum//extractfactor(index)
    if index != 0: #Division by 1 is irrelevant
        if count1s(index)%2 == 0:
            sum -= dp[index]
        else:
            sum += dp[index]

#Use gcd to simplify
nominator = sum
denominator = curnum

def gcd(a,b):
    big = max(a,b)
    small = min(a,b)

    if small == 0:
        return big

    right = big%small

    return gcd(small,right)

curgcd = gcd(denominator,nominator)
nominator =  nominator//curgcd
denominator = denominator//curgcd

print(f"{nominator}/{denominator}")
