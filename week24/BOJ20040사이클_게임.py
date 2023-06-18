import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
ans = 0
def find(x):
    if x == parent[x]:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp

def union(x,y,idx):
    global ans
    rx = find(x)
    ry = find(y)
    if rx != ry:
        parent[rx] = ry
    elif ans == 0:
        ans = idx

for i in range(m):
    a,b = map(int,input().split())
    union(a,b,i+1)
print(ans)