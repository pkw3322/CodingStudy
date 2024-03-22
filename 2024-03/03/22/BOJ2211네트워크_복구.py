from heapq import heappop,heappush
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
lines = [[] for _ in range(n+1)]
ans = []
def dijkstra(start):
    distance = [sys.maxsize for _ in range(n+1)]
    distance[start] = 0
    heap = [(0,start,0)]
    while heap:
        cnt,cur,before = heappop(heap)
        if distance[cur] < cnt :
            continue
        if before != 0:
            ans.append((before,cur))
        for weight,next in lines[cur]:
            if distance[next] > cnt + weight:
                distance[next] = cnt + weight
                heappush(heap,(cnt+weight,next,cur))
    return distance

for _ in range(m):
    a,b,c = map(int,input().split())
    lines[a].append((c,b))
    lines[b].append((c,a))

dijkstra(1)

print(len(ans))
for a,b in ans:
    print(a,b)