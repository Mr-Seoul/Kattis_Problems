def lookup(str,index):
    if -1 < index < len(str):
        return str[index]
    else:
        return " "

def lvStr(str, n):
    minAct = 2
    for i in range(0,n):
        if str[i-1:i+1] == "vl" or str[i:i+2] == "vl":
           minAct = min(minAct,1)
        if str[i] == 'l' or str[i] == 'v':
            minAct = min(minAct,1)
        if str[i-1:i+1] == "lv" or str[i:i+2] == "lv":
           minAct = min(minAct,0)

        if str[i] == 'l' and (lookup(str,i-2) == 'v' or lookup(str,i+2)=='v'):
           minAct = min(minAct,1)
        if str[i] == 'v' and (lookup(str,i-2) == 'l' or lookup(str,i+2)=='l'):
           minAct = min(minAct,1)
    return minAct
        
n = int(input())
str = input()
print(lvStr(str,n))