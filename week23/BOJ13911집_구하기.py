import sys
from heapq import heappush,heappop

input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int,input().split())
graph = [[] for _ in range(v+3)]
mac = []
star = []
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

macNum,macVal = map(int,input().split())
mac = list(map(int,input().split()))

starNum,starVal = map(int,input().split())
star = list(map(int,input().split()))
 
for i in mac:
    graph[v+1].append((0,i))
    graph[i].append((0,v+1))
for i in star:
    graph[v+2].append((0,i))
    graph[i].append((0,v+2))

def dijkstra(start):
    h = []
    dp = [INF]*(v+3)
    dp[start] = 0
    heappush(h,(0,start))
    while h:
        w,cur = heappop(h)
        if dp[cur] != w:
            continue

        for nw,next in graph[cur]:
            nextW = nw + w
            if next > v:
                continue
            if dp[next] > nextW:
                dp[next] = nextW
                heappush(h,(nextW,next))
    return dp

macCost = dijkstra(v+1)
starCost = dijkstra(v+2)
ans = sys.maxsize
for i in range(1,v+1):
    if i in mac or i in star:
        continue
    if macCost[i] <= macVal and starCost[i] <= starVal:
        ans = min(ans,macCost[i]+starCost[i])
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)