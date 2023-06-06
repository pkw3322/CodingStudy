import sys
from heapq import heappush,heappop

input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int,input().split())
dp = [sys.maxsize]*(n+1)
dp[s] = 0
h = []
heappush(h,(0,s))
while h:
    cnt,cur = heappop(h)
    for next,d in graph[cur]:
        wei = cnt + d
        if dp[next] > wei:
            dp[next] = wei
            heappush(h,(wei,next))

print(dp[t])
