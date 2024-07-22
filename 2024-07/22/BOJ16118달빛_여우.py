import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
mountains = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    mountains[a].append((b,c*2))
    mountains[b].append((a,c*2))

def wolf(start,graph):
    q = []
    heappush(q,(0,start,0))
    visited = [[inf]*2 for _ in range(n+1)]
    visited[start] = [0,inf]
    while q:
        dist, now, state = heappop(q)
        if visited[now][state] < dist:
            continue
        for next, cost in graph[now]:
            if state:
                cost *= 2
            else:
                cost //= 2
            if visited[next][state^1] > dist+cost:
                visited[next][state^1] = dist+cost
                heappush(q,(dist+cost,next,state^1))
    return visited

def fox(start,graph):
    q = []
    heappush(q,(0,start))
    visited = [inf] * (n+1)
    visited[start] = 0
    while q:
        dist, now = heappop(q)
        if visited[now] < dist:
            continue
        for next, cost in graph[now]:
            if visited[next] > dist+cost:
                visited[next] = dist+cost
                heappush(q,(dist+cost,next))
    return visited

wolf_dist = wolf(1,mountains)
fox_dist = fox(1,mountains)

answer = 0
for i in range(2,n+1):
    wolf_min_dist = min(wolf_dist[i])
    if wolf_min_dist > fox_dist[i]:
        answer += 1

print(answer)
