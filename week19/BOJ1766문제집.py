import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())
degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

def topo():
    res = []
    q = []
    
    for i in range(n+1):
        if degree[i] == 0:
            heapq.heappush(q,i)

    while q:
        cur = heapq.heappop(q)
        res.append(cur)
        for i in graph[cur]:
            degree[i] -= 1
            if degree[i] == 0:
                heapq.heappush(q,i)
            
    for i in range(1,len(res)):
        print(res[i],end=' ')

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

topo()