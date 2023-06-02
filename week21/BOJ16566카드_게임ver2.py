import sys
from bisect import bisect_right

input = sys.stdin.readline

n,m,k = map(int,input().split())
cards = sorted(map(int,input().split()))
chuls = list(map(int,input().split()))
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp
def union(x,y):
    rootX = find(x)
    rootY = find(y)
    if rootX > rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

for chul in chuls:
    idx = bisect_right(cards,chul)
    idx = find(idx)
    print(cards[idx])
    union(idx,idx+1)