import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,root,q = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
toKnow = []

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in range(q):
    toKnow.append(int(input()))

def dfs(cur):
    visited[cur] = 1
    queue = deque([cur])
    while queue:
        cur = queue.popleft()
        for nex in graph[cur]:
            if visited[nex] == 0:
                visited[cur] += dfs(nex)
    return visited[cur]

dfs(root)

for i in toKnow:
    print(visited[i])