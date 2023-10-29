import sys
from collections import deque
input = sys.stdin.readline


visited = []
ans = 0

def bfs(i,j,num):
    global ans
    queue = deque([(i,j)])
    isSwimPool = True
    visited[i][j] = True
    cnt = 1
    while queue:
        cx,cy = queue.popleft()

        for dist in range(4):
            nx,ny = cx + dx[dist],cy + dy[dist]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                isSwimPool = False
                continue
            if board[nx][ny] <= num and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1
    if isSwimPool:
        ans += cnt

n,m = map(int,input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for height in range(1,9):
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] <= height and not visited[i][j]:
                bfs(i,j,height)


print(ans)