import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n+1)]
    
def dfs(start):
    global graph
    global visited
    visited[start] = True
    if len(graph[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in graph[start]:
            if not visited[i]:
                dfs(i)
                dp[start][1] += min(dp[i][0],dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0],dp[1][1]))