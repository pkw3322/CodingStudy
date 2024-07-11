import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())
powers = list(map(int,input().split()))
graphs = []
parent = [i if i not in powers else 0 for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graphs.append((c,a,b))
graphs.sort()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px > py:
        parent[py] = px
    else:
        parent[px] = py
ans = 0
for weight,a,b in graphs:
    if find(a) != find(b):
        union(a,b)
        ans += weight

print(ans)