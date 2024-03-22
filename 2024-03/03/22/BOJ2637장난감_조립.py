import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

toys = [[] for _ in range(n+1)]
needs = [[0]*(n+1) for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    toys[b].append((a,c))
    degree[a] += 1

q = deque()
base = []
for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)
        base.append(i)

while q:
    cur = q.popleft()
    for next, cnt in toys[cur]:
        if cur in base:
            needs[next][cur] += cnt
        else:
            for i in range(1,n+1):
                needs[next][i] += needs[cur][i]*cnt
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

for i in range(1,n+1):
    if needs[n][i] != 0:
        print(i, needs[n][i])
