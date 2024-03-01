import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
sea = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

shark = [0,0]
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark = [i,j]


cnt = 0

def dfs(x,y):
    visited = [[0]*n for _ in range(n)]
    q = deque([[x,y]])
    cand = []
    visited[x][y] = 1
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[nx][ny]:
                if sea[nx][ny] == 0:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append([nx,ny])
                elif sea[x][y] > sea[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    cand.append([visited[nx][ny]-1,nx,ny])
                elif sea[x][y] == sea[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append([nx,ny])
    return sorted(cand,key = lambda x:(x[0],x[1],x[2]))

x,y = shark
size = [2,0]
while True:
    sea[x][y] = size[0]
    cand = deque(dfs(x,y))

    if not cand:
        break
    
    count,cx,cy = cand.popleft()
    cnt += count
    size[1] += 1
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    sea[x][y] = 0
    x,y = cx,cy

print(cnt)