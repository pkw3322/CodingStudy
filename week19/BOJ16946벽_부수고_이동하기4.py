import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
mod = 10
arr = [list(map(int,input().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
zeroArr = [[0]*m for _ in range(n)]
g = 1
infoDict = {}
infoDict[0] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        zeroArr[x][y] = g
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if -1 < nx < n and -1 < ny < m :
                if not visited[nx][ny] and arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            infoDict[g] = bfs(i,j)
            g += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            addSet = set()
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if -1 < nx < n and -1 < ny < m : 
                    addSet.add(zeroArr[nx][ny])
            for t in addSet:
                arr[i][j] += infoDict[t]
                arr[i][j] %= mod

for a in arr:
    print("".join(map(str,a)))
