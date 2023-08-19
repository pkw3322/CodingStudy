import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
cost = [0] + list(map(int,input().split()))

dp = [[0,cost[i]] for i in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n+1)]
    
def dfs(start):
    global visited
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][1] += dp[i][0]
            dp[start][0] += max(dp[i][0],dp[i][1])

dfs(1)
print(max(dp[1][1],dp[1][0]))