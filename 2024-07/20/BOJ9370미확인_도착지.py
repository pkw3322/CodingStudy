import sys
from heapq import heappush, heappop

input = sys.stdin.readline

test = int(input())

def dijkstra(start):
        dist = [sys.maxsize for _ in range(n+1)]
        dist[start] = 0
        heap = []
        heappush(heap, (0,start))
        while heap:
            curDist, cur = heappop(heap)
            if dist[cur] < curDist:
                continue
            for nxt, nxtCount in graphs[cur]:
                cost = curDist + nxtCount
                if cost < dist[nxt]:
                    dist[nxt] = cost
                    heappush(heap, (cost, nxt))
        return dist

for _ in range(test):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())
    graphs = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int, input().split())
        graphs[a].append((b,d))
        graphs[b].append((a,d))
    targets = []
    for _ in range(t):
        targets.append(int(input()))
    sDist = dijkstra(s)
    gDist = dijkstra(g)
    hDist = dijkstra(h)
    ans = []
    for target in targets:
        if sDist[target] == sDist[g] + gDist[h] + hDist[target] or sDist[target] == sDist[h] + hDist[g] + gDist[target]:
            ans.append(target)
    ans.sort()
    print(*ans)
    