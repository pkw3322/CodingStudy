import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[sys.maxsize]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    bus[a][b] = min(c,bus[a][b])
for i in range(1,n+1):
    bus[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            bus[i][j] = min(bus[i][j],bus[i][k]+bus[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j] == sys.maxsize:
            print(0,end=' ')
        else:
            print(bus[i][j],end=' ')
    print()
