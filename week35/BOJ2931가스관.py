from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def direct(s):
    if s == '|':
        return [1, 3]
    elif s == '-':
        return [0, 2]
    elif s == '+' or s == 'M' or s == 'Z':
        return [0, 1, 2, 3]
    elif s == '1':
        return [0, 1]
    elif s == '2':
        return [0, 3]
    elif s == '3':
        return [2, 3]
    elif s == '4':
        return [1, 2]

def bfs(x, y, dir):
    global fx, fy
    q = deque()
    q.append([x, y, dir])
    c[x][y] = 1
    while q:
        x, y, dir = q.popleft()
        for d in dir:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n and not c[nx][ny]:
                if a[nx][ny] != '.':
                    c[nx][ny] = 1
                    ndir = direct(a[nx][ny])
                    q.append([nx, ny, ndir])
                else:
                    if a[x][y] == 'M' or a[x][y] == 'Z':
                        continue
                    if not fx and not fy:
                        fx, fy = nx + 1, ny + 1
                    nd = (d+2) % 4
                    if nd not in checkList:
                        checkList.append(nd)

m, n = map(int, input().split())
c = [[0] * n for _ in range(m)]

a = []
for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == 'M':
            sx, sy = i, j
        elif row[j] == 'Z':
            zx, zy = i, j

checkList, fx, fy = [], 0, 0
bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(m):
    for j in range(n):
        if a[i][j] != '.' and not c[i][j]:
            bfs(i, j, direct(a[i][j]))
checkList.sort()

if len(checkList) == 4:
    print(fx, fy, '+')
else:
    blockList = ['|', '-', '1', '2', '3', '4']
    for s in blockList:
        if checkList == direct(s):
            print(fx, fy, s)
