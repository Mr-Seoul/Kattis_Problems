def equivalent(str1, str2):
    for i in range(0,min(len(str1),len(str2))):
        if str1[i] != str2[i]:
            return False
    return True

def valid(str,pattern):
    for i in range(0,len(str)):
        if str[i] != pattern[i%len(pattern)]:
            return False
    return True

def splitByCh(str,seperator):
    curSplit = []
    curStr = ""
    for i in range(0,len(str)):
        if (str[i] == seperator or i == len(str) - 1) and curStr != "":
            curSplit.append(curStr)
            curStr = ""
        curStr += str[i]
        
    return curSplit


def findPattern(str):
    for j in range(1,len(str)+1):
        subStr = str[0:j]
        if valid(str,subStr):
            return j
    else:
        return -1

n = int(input())

for i in range(0,n):
    str = input()
    print(findPattern(str))