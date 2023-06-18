import sys
from collections import deque

input = sys.stdin.readline
q = deque()
m,n,h = map(int,input().split())
tomatos = [[[]]*(n) for _ in range(h)]
visited = [[[-1]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        arr = list(map(int,input().split()))
        tomatos[i][j] = arr
        for k in range(m):
            if arr[k] == 1:
                q.append((i,j,k,0))
                visited[i][j][k] = 0

dir = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

while q:
    ch,cn,cm,cnt = q.popleft()
    for dh,dn,dm in dir:
        nh = ch + dh
        nn = cn + dn
        nm = cm + dm
        if 0<=nh<h and 0<=nn<n and 0<=nm<m and visited[nh][nn][nm] == -1 and tomatos[nh][nn][nm] != -1:
            visited[nh][nn][nm] = cnt+1
            q.append((nh,nn,nm,cnt+1))

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if visited[i][j][k] == -1 and tomatos[i][j][k] != -1:
                print(-1)
                exit(0)
            ans = max(ans,visited[i][j][k])
print(ans)