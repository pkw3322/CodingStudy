import sys
from heapq import heappush,heappop

n = int(input())
stations =[]

for i in range(n):
    a,b = map(int,input().split())
    stations.append((a,b))
    
l,p = map(int,input().split())
stations.append((l,p))
stations.sort()

cur = 0
cnt = 0
heap = []
for i in range(n+1):
    dist = stations[i][0] - cur
    cur = stations[i][0]
    if p < dist:
        while p < dist:
            if len(heap) > 0:
                p += (-1 * heappop(heap))
                cnt += 1
            else :
                cnt = -1
                break
        if cnt == -1:
            break
    p -= dist
    heappush(heap,-1*stations[i][1])

print(cnt)