import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())

indexA = [0]*101
indexB = [0]*101

ans = []

def getMinMaxValue():
    copiedA = deepcopy(indexA)
    copiedB = deepcopy(indexB)
    minSum = 0
    curA = getLastIndex(copiedA,1)
    curB = getLastIndex(copiedB,100,True)
    minV = min(copiedA[curA],copiedB[curB])
    copiedA[curA] -= minV
    copiedB[curB] -= minV
    while curA != -1 and curB != -1:
        minSum = max(minSum, curA+curB)
        curA = getLastIndex(copiedA,curA)
        curB = getLastIndex(copiedB,curB,True)

        minV = min(copiedA[curA],copiedB[curB])
        copiedA[curA] -= minV
        copiedB[curB] -= minV
    return minSum

def getLastIndex(arr,startIndex,isReverse=False):
    if isReverse:
        for i in range(startIndex,-1,-1):
            if arr[i] != 0:
                return i
    else:
        for i in range(startIndex,len(arr)):
            if arr[i] != 0:
                return i
    return -1
for _ in range(n):
    x,y = map(int, input().split())
    indexA[x] += 1
    indexB[y] += 1
    ans.append(str(getMinMaxValue()))

print("\n".join(ans))