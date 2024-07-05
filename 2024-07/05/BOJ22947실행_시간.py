import sys
from heapq import heappop, heappush
from copy import deepcopy
from itertools import combinations

input = sys.stdin.readline

n,m,k = map(int, input().split())
costs = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

def calCost(indegree, costs):
    q = []
    heappush(q, (costs[1],1))
    ans = [0]*(n+1)
    ans[1] = costs[1]
    flow = []
    while q:
        cCost, now = heappop(q)
        flow.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            ans[i] = max(ans[i], ans[now] + costs[i])
            if indegree[i] == 0:
                heappush(q, (ans[i], i))

    return flow, max(ans)

for _ in range(m):
    f,t = map(int, input().split())
    graph[f].append(t)
    indegree[t] += 1

firstIndegree = deepcopy(indegree)
workFlow, minCost = calCost(firstIndegree, costs)

for arr in combinations(range(2,n+1), k):
    if workFlow[-1] in arr:
        continue
    tempCosts = deepcopy(costs)
    for i in arr:
        tempCosts[i] = 0
    tempIndegree = deepcopy(indegree)
    _, curCost = calCost(tempIndegree, tempCosts)
    minCost = min(minCost, curCost)

print(minCost)