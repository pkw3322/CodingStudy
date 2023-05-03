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
    dp[start] = 0
    heap = []
    heappush(heap,[0,start])
    while heap:
        weight,cur = heappop(heap)
        for next,nweight in s[cur]:
            w = weight + nweight
            if dp[next] > w:
                dp[next] = w
                heappush(heap,[w,next])
    return dp

first = dijkstra(1)
v1Arr = dijkstra(v1)
v2Arr = dijkstra(v2)
ans = min(first[v1] + v1Arr[v2] + v2Arr[n],first[v2] + v2Arr[v1] + v1Arr[n])
if ans < INF:
    print(ans)
else:
    print(-1)