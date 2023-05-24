import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a,b,c = map(int,input().split())
    arr.append((a,b,c,i))

edges = []
for i in range(3):
    arr.sort(key = lambda x:x[i])
    for j in range(1,n):
        edges.append((abs(arr[j-1][i] - arr[j][i]),arr[j-1][3],arr[j][3]))
parent = [i for i in range(n)]
def find(x):
    if parent[x] == x:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp

def union(x,y):
    xRoot = find(x)
    yRoot = find(y)
    if xRoot != yRoot:
        parent[xRoot] = yRoot

ans = 0
edges.sort()
for edge in edges:
    value,idx1,idx2 = edge
    if find(idx1) != find(idx2):
        union(idx1,idx2)
        ans += value
print(ans)