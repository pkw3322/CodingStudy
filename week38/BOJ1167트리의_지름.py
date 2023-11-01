import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
graphs = [[] for _ in range(v+1)]

for _ in range(v):
    arr = list(map(int,input().split()))
    for idx in range(1,len(arr)-2,2):
        graphs[arr[0]].append((arr[idx],arr[idx+1]))

def bfs(start):
    visited = [-1]*(v+1)
    q = deque([start])
    visited[start] = 0
    maxNodes = [0,0]
    while q:
        cur = q.popleft()
        for to,weight in graphs[cur]:
            if visited[to] == -1:
                visited[to] = visited[cur] + weight
                q.append(to)
                if maxNodes[0] < visited[to]:
                    maxNodes = visited[to],to
    return maxNodes

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)