import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
ways = [list(map(int,input().split())) for _ in range(n)]

travel = list(map(int,input().split()))
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
    else:
        parent[x] = y

for i in range(n):
    for j in range(n):
        if ways[i][j]:
            union(i+1,j+1)
flag = True
for i in range(m-1):
    if find(travel[i]) != find(travel[i+1]):
        print("NO")
        flag = False
        break
if flag:
    print("YES")