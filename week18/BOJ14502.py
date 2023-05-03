from collections import deque

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(tempArr):
    q = deque()
    for i in range(n):
        for j in range(m):
            if tempArr[i][j] == 2:
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if -1 < nx < n and -1 < ny < m:
                if tempArr[nx][ny] == 0:
                    tempArr[nx][ny] = 2
                    q.append((nx,ny))
    global ans
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tempArr[i][j] == 0:
                cnt += 1
    ans = max(ans,cnt)

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
zeros=[]
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            zeros.append([i,j])
ans = 0
for i in range(len(zeros)):
    for j in range(i+1,len(zeros)):
        for k in range(j+1,len(zeros)):
            a = []
            for l in range(n):
                a.append([o for o in arr[l]])
            x,y = zeros[i]
            a[x][y] = 1
            x,y = zeros[j]
            a[x][y] = 1
            x,y = zeros[k]
            a[x][y] = 1
            bfs(a)
print(ans)
