import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
h = []
parents = [i for i in range(n+1)]

for i in range(1,n+1):
    heappush(h, [int(input()), 0, i])

for i in range(1,n+1):
    lines = list(map(int, input().split()))
    for j in range(1,n+1):
        if i == j:
            continue
        heappush(h, [lines[j-1], i, j])

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)
    if py == px:
        return True
    else:
        parents[py] = px
        return False

ans = 0
while h:
    cur_cost, f, t = heappop(h)
    if not union(f, t):
        ans += cur_cost
     
print(ans)