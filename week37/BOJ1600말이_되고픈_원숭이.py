import sys
from collections import deque   

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

hx = [-1,1,-1,1,-2,-2,2,2]
hy = [-2,-2,2,2,-1,1,-1,1]

def bfs():
    queue = deque([(0,0,0)])
    visited = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    while queue:
        cx,cy,cnt = queue.popleft()
        if cx == h-1 and cy == w-1:
            return  visited[cx][cy][cnt]-1
        if cnt < k:
            for i in range(8):
                nx,ny = cx + hx[i],cy + hy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if not visited[nx][ny][cnt+1] and not board[nx][ny]:
                    visited[nx][ny][cnt+1] = visited[cx][cy][cnt] + 1
                    queue.append((nx,ny,cnt+1))
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if not visited[nx][ny][cnt] and not board[nx][ny]:
                visited[nx][ny][cnt] = visited[cx][cy][cnt] + 1
                queue.append((nx,ny,cnt))

    return -1

k = int(input())
w,h = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(h)]

print(bfs())