import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
visited = [False]*(n+1)
dp = [[0,1] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):
    for next in graph[cur]:
        if not visited[next]:
            visited[next] = True
            dfs(next)
            dp[cur][1] += min(dp[next][0],dp[next][1])
            dp[cur][0] += dp[next][1]
    
visited[1] = True
dfs(1)
print(min(dp[1]))