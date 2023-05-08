import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
parent = [i for i in range(n)]
ans = 0

def find(x):
    if x == parent[x]:
        return x
    else :
        temp = find(parent[x])
        parent[x] = temp
        return temp

def union(x,y,idx):
    global ans
    px = find(x)
    py = find(y)
    if px != py:
        parent[py] = px
    elif ans == 0:
        ans = idx


for i in range(m):
    b,c = map(int,input().split())
    union(b,c,i+1)

print(ans)