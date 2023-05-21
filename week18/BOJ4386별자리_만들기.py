import sys
import math
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = []
edg = []
parent = [i for i in range(n+1)]
ans = 0

def dist(x1,y1,x2,y2) :
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)

def find(x):
    if parent[x] == x:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp

def union(x,y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rootx] = rooty
    
for i in range(n):
    a,b = map(float,input().split())
    arr.append((a,b))

for i in range(n-1):
    for j in range(i+1,n):
        edg.append((dist(arr[i][0],arr[i][1],arr[j][0],arr[j][1]),i,j))

edg.sort()

for e in edg:
    cost,i,j = e
    if find(i) != find(j):
        union(i,j)
        ans += cost

print(round(ans,2))
