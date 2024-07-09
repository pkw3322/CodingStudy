import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

def bfs(start):
    res = 1
    q = deque()
    q.append((start, 0))
    q.append((start, 1))
    visited = [[False]*2 for _ in range(n+1)]
    visited[start][0] = True
    visited[start][1] = True
    while q:
        now,dist = q.popleft()
        for i in range(1, n+1):
            if dist == 0 and graph[now][i] == 1 and not visited[i][0]:
                visited[i][0] = True
                res += 1
                q.append((i, 0))
            elif dist == 1 and graph[i][now] == 1 and not visited[i][1]:
                visited[i][1] = True
                res += 1
                q.append((i, 1))

    return res

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1

ans = [0]*(n+1)

for i in range(1,n+1):
    ans[i] = bfs(i)

for a in ans[1:]:
    print(n-a)