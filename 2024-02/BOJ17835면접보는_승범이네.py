import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra():
    h = []
    for i in meetings:
        heappush(h,(0,i))
        results[i] = 0
    while h:
        cost,pos = heappop(h)
        if results[pos] < cost:
            continue
        for weight,next in graph[pos]:
            if cost + weight < results[next]:
                results[next] = cost + weight
                heappush(h,(cost+weight,next))
            
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