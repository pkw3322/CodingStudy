import sys
from collections import deque

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
changeDirect = [(2, 3),(2, 3),(0, 1),(0, 1)]

def outOfRange(x,y):
    return not (0 <= x < n and 0 <= y < n) or home[x][y] == "*"

def bfs():
    visited = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
    for sx,sy,dir in q:
        visited[sx][sy][dir] = 0
    while q:
        cx,cy,cd = q.popleft()
        nx = cx + dx[cd]
        ny = cy + dy[cd]

        if outOfRange(nx,ny):
            continue
        
        if home[nx][ny] == "!":
            if visited[nx][ny][cd] == -1:
                visited[nx][ny][cd] = visited[cx][cy][cd]
                q.append((nx,ny,cd))
            else:
                if visited[cx][cy][cd] < visited[nx][ny][cd]:
                    visited[nx][ny][cd] = visited[cx][cy][cd]
                    q.append((nx,ny,cd))
            for nd in changeDirect[cd]:
                if visited[nx][ny][nd] == -1:
                    visited[nx][ny][nd] = visited[cx][cy][cd]+1
                    q.append((nx,ny,nd))
                else:
                    if visited[cx][cy][cd] < visited[nx][ny][nd]:
                        visited[nx][ny][nd] = visited[cx][cy][cd]+1
                        q.append((nx,ny,nd)) 
        elif home[nx][ny] == ".":
            if visited[nx][ny][cd] == -1:
                visited[nx][ny][cd] = visited[cx][cy][cd]
                q.append((nx,ny,cd))
            else:
                if visited[cx][cy][cd] < visited[nx][ny][cd]:
                    visited[nx][ny][cd] = visited[cx][cy][cd]
                    q.append((nx,ny,cd))  
    possible = []
    for c in visited[ex][ey]:
        if c == -1:
            continue
        possible.append(c)
    return min(possible)

n = int(input())

home = []
doors = []
for i in range(n):
    home.append(list(input().strip()))
    for j in range(n):
        if home[i][j] == "#":
            doors.append([i,j])
            home[i][j] = "."

sx,sy = doors[0]
ex,ey = doors[1]

q = deque()

for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if outOfRange(nx,ny):
        continue
    q.append((sx,sy,i))

print(bfs())