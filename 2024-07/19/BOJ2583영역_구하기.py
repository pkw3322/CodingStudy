import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*n for _ in range(m)]
def bfs(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    visited[y][x] = 1
    depth = 1
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[ny][nx] and not arr[ny][nx]:
                visited[ny][nx] = 1
                depth += 1
                q.append((nx,ny))
    return depth

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            arr[y][x] = 1

ans = []

for i in range(m):
    for j in range(n):
        if not visited[i][j] and not arr[i][j]:
            ans.append(bfs(j,i))
print(len(ans))
print(*sorted(ans))