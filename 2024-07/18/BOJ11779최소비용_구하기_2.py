import sys
from heapq import heappush, heappop
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
m = int(input())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graphs[a].append((c, b))

start, end = map(int, input().split())

q = []
heappush(q, (0, start,[start]))
visited = [0]*(n+1)

while q:
    cost, cur, prev = heappop(q)
    if cur == end:
        print(cost)
        print(len(prev))
        print(*prev)
        break
    if visited[cur]:
        continue
    visited[cur] = 1
    for nCost, nNode in graphs[cur]:
        if visited[nNode] == 0:
            temp = deepcopy(prev)
            temp.append(nNode)
            heappush(q, (cost+nCost, nNode, temp))

