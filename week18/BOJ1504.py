from heapq import heappush,heappop
import sys

n,e = map(int,sys.stdin.readline().split())
s = [[] for _ in range(n+1)]

INF = sys.maxsize

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    s[a].append((b,c))
    s[b].append((a,c))
v1,v2 = map(int,sys.stdin.readline().split())

def dijkstra(start):
    dp = [INF for _ in range(n+1)]
    heap = []
    dp[start] = 0
    heappush(heap,[0,start])
    while heap:
        w,c = heappop(heap)
        for nc,nw in s[c]:
            wei = nw + w
            if dp[nc] > wei:
                dp[nc] = wei
                heappush(heap,[wei,nc])
    return dp

f = dijkstra(1)
v1Arr = dijkstra(v1)
v2Arr = dijkstra(v2)

ans = min(f[v1] + v1Arr[v2] + v2Arr[n],f[v2] + v2Arr[v1] + v1Arr[n])

if ans < INF:
    print(ans)
else:
    print(-1)