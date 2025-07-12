def solution(str1,str2):
    sol = 1
    for i in range(0,len(str1)):
        if str1[i] != str2[i]:
            sol += 1
    return sol


initialLine = input()
finalLine = input()

print(solution(initialLine,finalLine))