import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

parents = [i for i in range(n+1)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px > py:
        parents[py] = px
    else:
        parents[px] = py

edges = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
    union(a,b)

for i in range(1,n+1):
    find(i)

pgroups = {i:[] for i in set(parents[1:])}

for i in range(1,n+1):
    pgroups[parents[i]].append(i)


def bfs(start):
    dist = 0
    q = deque([start])
    visited = set(q)
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for node in edges[cur]:
                if node in visited:
                    continue
                visited.add(node)
                q.append(node)
        dist += 1
    return dist

ans = []

for group in pgroups.values():
    min_dist = sys.maxsize
    pres = 0
    for node in group:
        cur = bfs(node)
        if cur < min_dist:
            min_dist = cur
            pres = node
    ans.append(pres)

print(len(ans))
print('\n'.join(map(str,sorted(ans))))