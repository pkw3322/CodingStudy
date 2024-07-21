import sys
from collections import deque

input = sys.stdin.readline

n, m, x = map(int, input().split())
high = [[] for _ in range(n+1)]
low = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    high[a].append(b)
    low[b].append(a)

def bfs(start,graph):
    q = deque()
    q.append(start)
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

print(1+bfs(x,low),n-bfs(x,high))
