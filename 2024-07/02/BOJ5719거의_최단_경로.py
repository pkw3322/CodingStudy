import sys
from collections import deque

input = sys.stdin.readline

def findMinPath(start, costList):
    ans = [[] for _ in range(n)]
    q = deque()
    costList[start] = 0
    q.append((start, 0))
    while q:
        now, cost = q.popleft()
        if cost > costList[now]:
            continue
        for nex, nCost in roads[now]:
            if nCost != -1:
                if costList[nex] > costList[now] + nCost:
                    costList[nex] = costList[now] + nCost
                    q.append((nex, nCost))
                    ans[nex].clear()
                    ans[nex].append(now)

                elif costList[nex] == costList[now] + nCost:
                    ans[nex].append(now)
    return ans

def bfs(end, roads, miniRoads, visited):
    q = deque()
    q.append(end)
    while q:
        now = q.popleft()
        for i in miniRoads[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
            for j in roads[i]:
                if j[0] == now:
                    roads[i][roads[i].index(j)] = (j[0], -1)
    return roads

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    start, end = map(int,input().split())
    roads = [[] for _ in range(n)]
    miniRoads = []
    for _ in range(m):
        a,b,c = map(int,input().split())
        roads[a].append((b,c))
    costList = [int(1e10)]*n

    miniRoads = findMinPath(start,costList)
    visited = [False]*n
    
    bfs(end, roads, miniRoads, visited)
    
    costList = [int(1e10)]*n
    findMinPath(start, costList)
    
    if costList[end] == int(1e10):
        print(-1)
    else:
        print(costList[end])