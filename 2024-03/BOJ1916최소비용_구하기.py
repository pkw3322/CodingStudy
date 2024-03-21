from heapq import heappush, heappop
import sys

input = sys.stdin.readline

def dijkstra():
    heap = []
    heappush(heap,(0,start))
    while heap:
        cost, cur = heappop(heap)
        if distance[start][cur] < cost:
            continue
        for v,e in bus[cur]:
            if distance[start][e] > cost + v:
                distance[start][e] = cost + v
                heappush(heap,(distance[start][e],e))
    

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
distance = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s,e,v = map(int,input().split())
    bus[s].append((v,e))

start,end = map(int,input().split())

dijkstra()

print(distance[start][end])