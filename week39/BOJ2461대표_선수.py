import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
indexs = [1]* 1001
maxVal = -1
hq = []

for i in range(n):
    lis = list(map(int,input().split()))
    lis.sort()
    maxVal = max(maxVal,lis[0])
    arr.append(lis)
    heappush(hq,(arr[i][0], i))

ans = sys.maxsize
while hq:
    start = heappop(hq)
    minVal = start[0]
    index = start[1]

    ans = min(ans, maxVal - minVal)
    if indexs[index] == m:
        break
    heappush(hq,(arr[index][indexs[index]],index))
    maxVal = max(maxVal,arr[index][indexs[index]])
    indexs[index] += 1

print(ans)