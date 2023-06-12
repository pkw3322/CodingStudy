import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    cnt = 0
    while q:
        cnt += 1
        while fire and fire[0][2] < cnt:
            cx,cy,ccnt = fire.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if building[nx][ny] == '.' or building[nx][ny] == '@':
                        building[nx][ny] = '*'
                        fire.append((nx,ny,ccnt+1))
        while q and q[0][2] < cnt:
            cx,cy,ccnt = q.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if building[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny,ccnt+1))
                else :
                    print(cnt)
                    return 
    print("IMPOSSIBLE")
for _ in range(t):
    w,h = map(int,input().split())
    building = []
    visited = [[False]*w for _ in range(h)]
    q = deque()
    fire = deque()
    for i in range(h):
        building.append(list(input().strip()))
        for j in range(w):
            if building[i][j] == '@':
                visited[i][j] = True
                q.append((i,j,0))
            if building[i][j] == '*':
                fire.append((i,j,0))
    bfs()
    