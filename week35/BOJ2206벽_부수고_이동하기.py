from collections import deque

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs():
    while q:
        cr, cc, isBreak = q.popleft()
        if cr == n-1 and cc == m-1:
            return visited[cr][cc][isBreak]
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if walls[nr][nc] == 1 and not isBreak:
                    visited[nr][nc][1] = visited[cr][cc][0] + 1
                    q.append((nr, nc, 1))
                elif walls[nr][nc] == 0 and visited[nr][nc][isBreak] == 0:
                    visited[nr][nc][isBreak] = visited[cr][cc][isBreak] + 1
                    q.append((nr,nc,isBreak))
    return -1 

n,m = map(int,input().split())
walls = []
for i in range(n):
    walls.append(list(map(int,input())))

visited = [[[0,0] for _ in range(m)] for _ in range(n)]

visited[0][0][0] = 1
q = deque([(0,0,0)])

print(bfs())