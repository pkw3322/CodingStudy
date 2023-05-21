from collections import deque

import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque([(0,0)])
    melt = deque([])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if cheeze[nx][ny] == 0:
                        queue.append((nx,ny))
                    elif cheeze[nx][ny] == 1:
                        melt.append((nx,ny))
    for x,y in melt:
        cheeze[x][y] = 0
    return len(melt)


n,m = map(int,input().split())
cheeze = []
cnt = 0
for i in range(n):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])
time = 0
while True:
    visited = [[False]*(m+1) for _ in range(n+1)]
    meltCount = bfs()
    cnt -= meltCount
    if cnt == 0:
        print(time+1)
        print(meltCount)
        break
    time += 1