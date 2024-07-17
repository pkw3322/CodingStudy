import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
trains = []
for _ in range(n):
    a,b = map(int, input().split())
    if a > b:
        a,b = b,a
    trains.append((a,b))
d = int(input())

trains.sort(key=lambda x: (x[1], x[0]))

cnt = 0
h = []

for train in trains:
    a,b = train
    heappush(h, a)
    minStart = b - d

    while h and h[0] < minStart:
        heappop(h)
    cnt = max(cnt, len(h))
    
print(cnt)
