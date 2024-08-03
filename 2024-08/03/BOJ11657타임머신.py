import sys

input = sys.stdin.readline

def bellmanFord():
    dists[1] = 0
    for i in range(n):
        for j in range(m):
            cur, next, cost = graph[j]
            if dists[cur] != sys.maxsize and dists[next] > dists[cur] + cost:
                dists[next] = dists[cur] + cost
                if i == n-1:
                    return True
    return False

n, m = map(int, input().split())
graph = []
dists = [sys.maxsize] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

negativeCycle = bellmanFord()

if negativeCycle:
    print(-1)
else:
    for i in range(2, n+1):
        print(dists[i] if dists[i] != sys.maxsize else  -1)

