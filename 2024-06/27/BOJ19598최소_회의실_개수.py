import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

meetings = sorted([list(map(int, input().split())) for _ in range(n)])

rooms = []

while meetings:
    start, end = meetings.pop(0)
    if rooms and rooms[0] <= start:
        heappop(rooms)
    heappush(rooms, end)

print(len(rooms))
