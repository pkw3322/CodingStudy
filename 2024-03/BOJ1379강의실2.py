import sys
from heapq import heappop,heappush

input = sys.stdin.readline

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

lec = [0 for _ in range(n+1)]
graph.sort(key=lambda x: (x[1],x[2]))

lectureRoom = []
for i in range(1,n+1):
    heappush(lectureRoom,i)

minTime = []
for arr in graph:
    while minTime and minTime[0][0] <= arr[1]:
        endTime,room = heappop(minTime)
        heappush(lectureRoom,room)
    room = heappop(lectureRoom)
    heappush(minTime,[arr[2],room])
    lec[arr[0]] = room
print(max(lec))
for x in lec[1:]:
    print(x)
