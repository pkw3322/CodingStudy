import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isInRange(x,y):
    return 0 <= x < n and 0 <= y < n

def divideIsland(x,y):
    global count
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    ground[x][y] = count

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if isInRange(nx,ny) and not visited[nx][ny] and ground[nx][ny] == 1:
                visited[nx][ny] = True
                ground[nx][ny] = count
                q.append([nx,ny])

def getBridge(cnt):
    global ans
    dist = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if ground[i][j] == cnt:
                dist[i][j] = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if isInRange(ni,nj) and ground[ni][nj] == 0:
                        q.append([i,j])
                        break
    
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if not isInRange(nx,ny):
                continue
            if ground[nx][ny] > 0 and ground[nx][ny] != cnt:
                ans = min(ans,dist[cx][cy])
                return
            if ground[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[cx][cy] + 1
                q.append([nx,ny])

n = int(input())
ground = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count = 1
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if not visited[i][j] and ground[i][j] == 1:
            divideIsland(i,j)
            count += 1
            
for i in range(1,count):
    getBridge(i)
print(ans)