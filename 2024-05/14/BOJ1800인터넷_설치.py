import sys
import heapq

input = sys.stdin.readline

n,p,k = map(int,input().split())

arr = [[] for _ in range(n+1)]
max_cost = 0

for _ in range(p):
    a,b,w = map(int,input().split())
    arr[a].append((b,w))
    arr[b].append((a,w))
    max_cost = max(max_cost,w)


def dijkstra(totalCost):
    q = []
    heapq.heappush(q,(0,1))

    dist = [sys.maxsize for _ in range(n+1)]
    dist[1] = 0

    while q:
        cost, cur = heapq.heappop(q)
        if dist[cur] < cost:
            continue
        for next, next_cost in arr[cur]:
            if totalCost < next_cost:
                if dist[next] > cost + 1:
                    dist[next] = cost + 1
                    heapq.heappush(q,(cost+1,next))
            else:
                if dist[next] > cost:
                    dist[next] = cost
                    heapq.heappush(q,(cost,next))
    return dist[n]

left = 0
right = max_cost
ans = sys.maxsize

while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid) <= k:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
