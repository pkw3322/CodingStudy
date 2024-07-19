import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px > py:
        parent[px] = py
    else:
        parent[py] = px

enemies = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(str,input().split())
    b = int(b)
    c = int(c)
    if a == 'E':
        enemies[b].append(c)
        enemies[c].append(b)
    elif a == 'F':
        if find(b) != find(c):
            union(b,c)

visited = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in enemies[i]:
        for k in enemies[j]:
            if find(i) != find(k) and not visited[i][k]:
                union(i,k)
                visited[i][k] = 1
                visited[k][i] = 1

ans = 0
for i in range(1,n+1):
    if i == parent[i]:
        ans += 1

print(ans)