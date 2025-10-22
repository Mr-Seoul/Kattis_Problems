import math

n = int(input())

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

for i in range(n):
    l1[i] -= 1
    l2[i] -= 1

class SortingArray:
    def __init__(self,arr):
        self.arr = arr
        self.inversions = 0

    def mergeSort(self):
        n = 1

        def mergeSortedArrays(start,A,B):
            index, indexA, indexB = (0,0,0)
            while indexA + indexB < len(A) + len(B):
                    if indexA < len(A) and indexB < len(B):
                        if A[indexA] < B[indexB]:
                            self.arr[start + index] = A[indexA]
                            indexA += 1
                            index += 1
                        else:
                            self.arr[start + index] = B[indexB]
                            indexB += 1
                            index += 1
                            self.inversions += len(A) - indexA
                    elif len(A) > indexA:
                        while len(A) > indexA:
                            self.arr[start+index] = A[indexA]
                            indexA += 1
                            index += 1
                        A = []
                    elif len(B) > indexB:
                        while len(B) > indexB:
                            self.arr[start+index] = B[indexB]
                            indexB += 1
                            index += 1
                        B = []

        while n < len(self.arr):
            for seg in range(0,math.ceil(len(self.arr)/(2*n))):
                min = 2*n*seg
                leftarr = self.arr[min:min+n]
                rightarr = self.arr[min+n:min+2*n]
                mergeSortedArrays(min,leftarr,rightarr)
            n *= 2
        
        return self.arr

map1 = [[0] for i in range(n)]
newl2 = [[0] for i in range(n)]

for i in range(n):
    map1[l1[i]] = i
for i in range(n):
    newl2[i] = map1[l2[i]]

Sortarr = SortingArray(newl2)
Sortarr.mergeSort()
print(Sortarr.inversions)
