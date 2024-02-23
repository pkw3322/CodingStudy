import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra():
    h = []
    for meeting in meetings:
        heappush(h,(0,meeting))
        results[meeting] = 0
    while h:
        cost, place = heappop(h)
        if results[place] < cost:
            continue
        for nCost,nPlace in graph[place]:
            if cost + nCost < results[nPlace]:
                results[nPlace] = cost + nCost
                heappush(h,(cost+nCost,nPlace))


n,m,k = map(int,input().split())

graph =[[] for _ in range(n+1)]

for _ in range(m):
    u,v,c = map(int,input().split())
    graph[v].append((c,u))
meetings = list(map(int,input().split()))

mPlace,mCost = 0,0
results = [sys.maxsize for _ in range(n+1)]

dijkstra()

for i in range(n+1):
    if results[i] != sys.maxsize and mCost < results[i]:
        mCost = results[i]
        mPlace = i

print(mPlace)
print(mCost)