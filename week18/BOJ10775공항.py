import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
arr = [int(input()) for _ in range(P)]
parent = [i for i in range(G+1)]
cnt = 0

def find(x):
    if x == parent[x]:
        return x
    root = find(parent[x])
    parent[x] = root
    return root

def union(x,y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rootx] = rooty

for i in range(P):
    airplane = arr[i]
    root = find(airplane)
    if root == 0:
        break
    union(root,root-1)
    cnt += 1
    
print(cnt)