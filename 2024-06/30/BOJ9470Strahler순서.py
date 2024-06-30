import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    k,m,p = map(int, input().split())
    indegree = [0]*(m+1)
    graph = [[] for _ in range(m+1)]
    strahler = [[0,0] for _ in range(m+1)]
    orders = [0]*(m+1)

    for _ in range(p):
        a,b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    q = deque()

    for i in range(1,m+1):
        if indegree[i] == 0:
            strahler[i] = [1,1]
            q.append(i)
            
    while q:
        now = q.popleft()
        if strahler[now][1] >= 2:
            orders[now] = strahler[now][0] + 1
        else :
            orders[now] = strahler[now][0]
        for i in graph[now]:
            indegree[i] -= 1
            if strahler[i][0] < orders[now]:
                strahler[i][0] = orders[now]
                strahler[i][1] = 1
            elif strahler[i][0] == orders[now]:
                strahler[i][1] += 1

            if indegree[i] == 0:
                q.append(i)

    ans.append((k, max(orders)))

for a in ans:
    print(a[0], a[1])