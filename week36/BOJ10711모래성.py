import sys
from collections import deque

input = sys.stdin.readline
def outOfRange(x,y):
    return 0 > x or x >= h or 0 > y or y >= w

h,w = map(int,input().split())
dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,-1,1,-1,1]
sandCastle = [list(input()) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]

queue = deque()
for i in range(h):
    for j in range(w):
        if sandCastle[i][j] == '.':
            sandCastle[i][j] = 0
            queue.append((i,j))
        else:
            sandCastle[i][j] = int(sandCastle[i][j])

ans = 0

while len(queue):
    x,y = queue.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if outOfRange(nx,ny):
            continue
        if sandCastle[nx][ny] != 0:
            sandCastle[nx][ny] -= 1
            if sandCastle[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                ans = max(ans, visited[nx][ny])
                queue.append((nx,ny))

print(ans) 