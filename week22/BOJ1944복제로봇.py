import sys
from heapq import heappush,heappop
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
keys = []
res = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'S' or arr[i][j] == 'K':
            keys.append((i,j))

def bfs(sx,sy,ex,ey):
    global keyDict,keyCnt
    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((sx,sy,0))
    visited[sx][sy] = True
    while q:
        cx,cy,cnt = q.popleft()
        if (ex,ey) == (cx,cy):
            return cnt
        for i in range(4):
            nx,ny = cx + dx[i],cy + dy[i]
            if 0 < nx < n and 0 < ny < n and not visited[nx][ny] and arr[nx][ny] != '1':
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return -1

parent = [i for i in range(m+1)]

def find(x):
    if parent[x] == x:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp

def union(x,y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        parent[rootX] = rootY
        return True
    else:
        return False

for i in range(m+1):
    for j in range(i+1,m+1):
        sx,sy = keys[i]
        ex,ey = keys[j]
        cnt = bfs(sx,sy,ex,ey)
        if cnt == -1:
            print(-1)
            exit(0)
        heappush(res,(cnt,i,j))

ans = 0
num = 0
while res:
    curCnt,i,j = heappop(res)
    if union(i,j):
        ans += curCnt
        num += 1
        if num == m:
            break

if num == m:
    print(ans)
else:
    print(-1)

