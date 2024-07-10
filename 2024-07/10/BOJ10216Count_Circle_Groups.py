import sys
import math

input = sys.stdin.readline

def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
def union(x, y):
    px = find(x)
    py = find(y)
    if px > py:
        parent[px] = py
    else:
        parent[py] = px

def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

test = int(input())

for _ in range(test):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    parent = [i for i in range(n)]

    for i in range(n):
        x1, y1, r1 = arr[i]
        for j in range(i+1, n):
            x2, y2, r2 = arr[j]
            if dist(x1, y1, x2, y2) <= r1 + r2:
                union(i, j)

    group = set()
    for i in range(n):
        x = find(i)
        if x not in group:
            group.add(x)

    print(len(group))