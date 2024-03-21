from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

sr,sc,sd = map(int,input().split())
er,ec,ed = map(int,input().split())

sr -= 1
sc -= 1
sd -= 1
er -= 1
ec -= 1
ed -= 1

def angle(x,y):
    return (x == 0 and y == 1) or (x == 1 and y == 0) or (x == 2 and y == 3) or (x == 3 and y == 2)

def bfs():
    q = deque()
    q.append((sr,sc,sd,0))
    visited = [[[0]*4 for _ in range(m)] for _ in range(n)]
    visited[sr][sc][sd] = 1
    while q:
        cr,cc,cd,cnt = q.popleft()
        if cr == er and cc == ec and cd == ed:
            return cnt
        for i in range(1,4):
            nr,nc = cr+dr[cd]*i,cc+dc[cd]*i
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1:
                    break
                if not visited[nr][nc][cd]:
                    visited[nr][nc][cd] = cnt + 1
                    q.append((nr,nc,cd,cnt+1))
        
        for nd in range(4):
            if nd == cd or angle(cd,nd):
                continue
            if not visited[cr][cc][nd]:
                visited[cr][cc][nd] = cnt + 1
                q.append((cr,cc,nd,cnt+1))
    return -1
print(bfs())