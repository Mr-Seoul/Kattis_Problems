a,b,c = tuple(map(int,input().split()))

whole = a*b // c
rem = a*b % c

whole = str(int(whole))
rem = "{:10f}".format(rem/c)

def finddot(strin):
    for i in range(0,len(strin)):
        print(i)
        if strin[i] == ".":
            return i

print(whole + rem[finddot(rem):len(rem)])