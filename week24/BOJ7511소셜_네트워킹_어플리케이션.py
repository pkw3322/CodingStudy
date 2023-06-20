import sys

input = sys.stdin.readline

t = int(input())

def find(parent,x):
    if x == parent[x]:
        return x
    temp = find(parent,parent[x])
    parent[x] = temp
    return temp

def union(parent,x,y):
    rx = find(parent,x)
    ry = find(parent,y)
    if rx != ry:
        parent[rx] = ry

def checking(parent,x,y):
    if find(parent,x) == find(parent,y):
        return 1
    return 0

for i in range(1,t+1):
    n = int(input())
    k = int(input())
    parent = [i for i in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
    m = int(input())
    print("Scenario "+str(i)+":")
    for _ in range(m):
        u,v = map(int,input().split())
        print(checking(parent,u,v))
    print()
