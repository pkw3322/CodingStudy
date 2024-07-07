import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

def throwStick(height, direct):
    if direct == 0:
        for i in range(C):
            if cave[R-height][i] == 'x':
                cave[R-height][i] = '.'
                return R-height, i
    else:
        for i in range(C-1, -1, -1):
            if cave[R-height][i] == 'x':
                cave[R-height][i] = '.'
                return R-height, i
    return -1, -1

def checkCluster(x, y):
    visited = [[False]*C for _ in range(R)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < R and 0 <= ny < C) and not visited[nx][ny]:
                if cave[nx][ny] == 'x':
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return visited

def getMinimumList(visited):
    minList = [-1]*C
    for y in range(C):
        for x in range(R-1, -1, -1):
            if visited[x][y] and minList[y] == -1:
                minList[y] = x
                break
            
    return minList

def getFallHeight(minList):
    minDiff = sys.maxsize
    for x, y in enumerate(minList):
        if y == -1:
            continue
        diff = 0
        for i in range(y+1, R):
            if cave[i][x] == 'x':
                break
            diff += 1
        minDiff = min(minDiff, diff)
    return minDiff

def falling(height, visited):
    for x in range(R-1, -1, -1):
        for y in range(C):
            if visited[x][y]:
                cave[x+height][y] = cave[x][y]
                cave[x][y] = '.'

turn = 0
for height in heights:
    x,y = throwStick(height, turn)
    turn ^= 1
    if x == -1 and y == -1:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not(0 <= nx < R and 0 <= ny < C) or cave[nx][ny] == '.':
            continue
        visited = checkCluster(nx, ny)
        minList = getMinimumList(visited)

        if R-1 in minList:
            continue
        fallHeight = getFallHeight(minList)
        falling(fallHeight, visited)

        break


for c in cave:
    print(''.join(c))