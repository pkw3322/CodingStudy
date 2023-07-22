import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def defuse(virus):
    q = deque(virus)
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    res = 0
    for x,y in q:
        visited[x][y] = 0
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and arr[nx][ny] != 1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[cx][cy] + 1
                    res = max(res,visited[nx][ny])
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and arr[i][j] != 1:
                return sys.maxsize
    return res

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
viruses = []

ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            viruses.append([i,j])

for v in combinations(viruses,m):
    ans = min(defuse(v),ans)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)