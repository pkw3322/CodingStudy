import sys

input = sys.stdin.readline

n = int(input())
w = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def solve(node):
    if visited[node] == 1:
        return max(dp[node][0], dp[node][1])
    
    visited[node] = 1
    dp[node][1] = w[node]

    for child in graph[node]:
        if visited[child] == 0:
            solve(child)
            dp[node][1] += dp[child][0]
            dp[node][0] += max(dp[child][0], dp[child][1])
    
    return max(dp[node][0], dp[node][1])

res = solve(1)

checked = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

def trace(node, p):
    if visited[node] == 1:
        return
    visited[node] = 1

    if p == 0:
        if dp[node][0] > dp[node][1]:
            checked[node] = 0

            for child in graph[node]:
                if visited[child] == 0:
                    trace(child, 0)
        else:
            checked[node] = 1

            for child in graph[node]:
                if visited[child] == 0:
                    trace(child, 1)
    else:
        checked[node] = 0

        for child in graph[node]:
            if visited[child] == 0:
                trace(child, 0)

trace(1, 0)

print(res)
for i in range(1, n+1):
    if checked[i] == 1:
        print(i, end=' ')
print()