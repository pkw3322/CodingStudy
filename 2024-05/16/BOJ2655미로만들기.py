import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
miro = []

for _ in range(n):
    lines = list(map(int,list(input().strip())))
    miro.append(lines)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
start = (0,0)
end = (n-1,n-1)

def inRange(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    q = deque()
    q.append(start)
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    while q:
        (x,y) = q.popleft()
        if (x,y) == end:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not inRange(nx,ny):
                continue
            if miro[nx][ny] == 0:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
            if miro[nx][ny] == 1:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y]:
                    visited[nx][ny] = visited[x][y]
                    q.append((nx,ny))
    return visited[n-1][n-1] - 1

print(bfs())
