import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n,m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(input().rstrip()))
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        if arr[i][j] == 'B':
            bx, by = i, j

def rolling(x, y, d):
    while True:
        x += dx[d]
        y += dy[d]
        if arr[x][y] == '#':
            return x-dx[d], y-dy[d]
        if arr[x][y] == 'O':
            break
    return x, y

def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    visited[rx][ry][bx][by] = 1
    
    while q:
        x, y, a, b, count = q.popleft()
        if count > 10:
            print(0)
            return
        if arr[x][y] == 'O':
            if count <= 10:
                print(1)
                return
            else:
                print(0)
                return
        for i in range(4):
            nrx, nry = rolling(x, y, i)
            nbx, nby = rolling(a, b, i)
            if arr[nbx][nby] == 'O':
                continue
            if nrx == nbx and nry == nby:
                if abs(nrx-x)+abs(nry-y) > abs(nbx-a)+abs(nby-b):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                q.append((nrx, nry, nbx, nby, count+1))
                visited[nrx][nry][nbx][nby] = 1
        count += 1
    print(0)


bfs()