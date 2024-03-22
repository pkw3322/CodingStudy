import sys

input = sys.stdin.readline

n,m = map(int,input().split())

heavy = [[] for _ in range(n+1)]
light = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    heavy[b].append(a)
    light[a].append(b)

def dfs(curList,root):
    cnt = 0
    for i in curList[root]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            cnt += dfs(curList,i)
    return cnt

mid = n//2
ans = 0

for i in range(1,n+1):
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    if dfs(heavy,i) > mid:
        ans += 1
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    if dfs(light,i) > mid:
        ans += 1
print(ans)