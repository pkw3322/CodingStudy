from heapq import heappop,heappush
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = sys.maxsize

def dijkstra(start):
    dp = [INF]*(v+1);
    dp[start] = 0
    heap = []
    heappush(heap,(0,start))
    while heap:
        cW,cC = heappop(heap)
        for next,nW in graph[cC]:
            wei = nW + cW
            if dp[next] > wei:
                dp[next] = wei
                heappush(heap,(wei,next))
    return dp
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

ans = dijkstra(start)
for i in range(1,len(ans)):
    if ans[i] < INF:
        print(ans[i])
    else:
        print("INF")