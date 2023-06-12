import sys
from collections import deque

input = sys.stdin.readline
w,h = map(int,input().split())
board = []
lasers = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]
ans = 0
def bfs(sx,sy,ex,ey):
    global ans
    q = deque()
    visited = [[[sys.maxsize]*4 for _ in range(w)] for _ in range(h)]
    for i in range(4):
        nx = sx+dx[i]
        ny = sy+dy[i]
        if 0<=nx<h and 0<=ny<w:
            if board[nx][ny] != '*':
                visited[nx][ny][i] = 0
                q.append((nx,ny,i))
    while q:
        cx,cy,dir = q.popleft()

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if 0<=nx<h and 0<=ny<w and board[nx][ny] != '*':
                cnt = visited[cx][cy][dir]
                if dir == 0 or dir == 2:
                    if i == 1 or i == 3:
                        cnt += 1
                else:
                    if i == 0 or i == 2:
                        cnt += 1
                if visited[nx][ny][i] == sys.maxsize:
                    visited[nx][ny][i] = cnt
                    q.append((nx,ny,i))
                else:
                    if visited[nx][ny][i] > cnt:
                        visited[nx][ny][i] = cnt
                        q.append((nx,ny,i))
    ans = min(visited[ex][ey])
for i in range(h):
    arr = list(input().strip())
    board.append(arr)
    for j in range(w):
        if board[i][j] == 'C':
            lasers.append((i,j))

bfs(lasers[0][0],lasers[0][1],lasers[1][0],lasers[1][1])
print(ans)