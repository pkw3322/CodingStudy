import sys
from collections import deque

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    preRank = list(map(int, input().split()))
    m = int(input())
    changePair = [list(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[preRank[i]].append(preRank[j])
            indegree[preRank[j]] += 1

    for a, b in changePair:
        if b in graph[a]:
            indegree[b] -= 1
            indegree[a] += 1
            graph[b].append(a)
            graph[a].remove(b)
        else:
            indegree[b] += 1
            indegree[a] -= 1
            graph[b].remove(a)
            graph[a].append(b)
    
    ans = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    if len(q) == 0:
        print("IMPOSSIBLE")
        continue
    result = True

    while q:
        if len(q) > 1:
            result = False
            break
        now = q.popleft()
        ans.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            elif indegree[i] < 0:
                result = False
                break
    if not result:
        print("?")
    elif len(ans) < n:
        print("IMPOSSIBLE")
    else:
        print(' '.join(map(str, ans)))