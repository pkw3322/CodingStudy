import sys
import math

input = sys.stdin.readline

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

n,m = map(int,input().split())

star = [tuple(map(int,input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else :
        parent[x] = y

for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

to_union = []
for i in range(1,n+1):
    for j in range(i+1,n+1):
        to_union.append((i,j,distance(star[i-1][0],star[i-1][1],star[j-1][0],star[j-1][1])))

to_union.sort(key=lambda x: x[2])
ans = 0
for a,b,c in to_union:
    if find(a) != find(b):
        union(a,b)
        ans += c

print(f'{ans:.2f}')