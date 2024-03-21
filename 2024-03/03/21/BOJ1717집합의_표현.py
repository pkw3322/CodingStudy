import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]  

def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def check(x,y):
    if find(x) == find(y):
        return "YES"
    else:
        return "NO"

ans = []
for _ in range(m):
    operation, a, b = map(int,input().split())
    if operation == 0:
        union(a,b)
    else:
        ans.append(check(a,b))
print('\n'.join(ans))