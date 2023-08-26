import sys
from heapq import heappop,heappush
input = sys.stdin.readline

n = int(input())
univs = []

for _ in range(n):
    univs.append(list(map(int,input().split())))

univs.sort(key = lambda x: (x[1]))
pq = []
for wei,time in univs:
    heappush(pq, wei)
    if len(pq) > time:
        heappop(pq)

print(sum(pq))