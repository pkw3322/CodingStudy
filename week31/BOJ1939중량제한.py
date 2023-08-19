import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px != py:
        parent[max(px,py)] = min(px,py)

def check(x,y):
    return find(x) == find(y)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append([-c,a,b])

s,e = map(int,input().split())

graph.sort()

for c,a,b in graph:
    c = abs(c)
    union(a,b)
    if check(s,e):
        print(c)
        break