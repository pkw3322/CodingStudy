import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int,input().split())
tomatoes = []
starts = []

for i in range(m):
    lines = list(map(int,input().split()))
    for j in range(n):
        if lines[j] == 1:
            starts.append((i,j))
    tomatoes.append(lines)

def isInbound(x,y):
    return 0<=x<m and 0<=y<n

def bfs(starts):
    q = deque(starts)
    visited = [[0]*n for _ in range(m)]
    for x,y in starts:
        visited[x][y] = 1

    while q:
        (x,y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInbound(nx,ny) or tomatoes[nx][ny] == -1 or visited[nx][ny] != 0:
                continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
    ans = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0 and tomatoes[i][j] == 0:
                return -1
            ans = max(ans,visited[i][j])
    return ans-1

print(bfs(starts))
        