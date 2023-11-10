import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n = int(input())
graph = []
visited = [False]*(1001)
maxD = 0
for _ in range(n):
    d,w = map(int,input().split())
    heappush(graph,(-w,d))
    maxD = max(maxD,d)

ans = 0
while graph:
    w,d = heappop(graph)
    w = -w
    for i in range(d, 0 ,-1):
        if visited[i]:
            continue
        visited[i] = True
        ans += w
        break
print(ans)