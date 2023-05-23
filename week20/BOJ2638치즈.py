import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
ans = 0
def checking():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return True
    return False
while checking():
    ans += 1
    toMelt = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0))
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx + dx[i],cy+dy[i]
            if -1 < nx < n and -1 < ny < m:
                if not visited[nx][ny]:
                    if arr[nx][ny] == 1:
                        toMelt[nx][ny] += 1
                    else :
                        q.append((nx,ny))
                        visited[nx][ny] = True
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and toMelt[i][j] >= 2:
                arr[i][j] = 0

print(ans)          