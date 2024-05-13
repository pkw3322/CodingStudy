import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
miro = []
start = (0,0)
ends = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(n):
    lines = list(input().strip())
    for j in range(m):
        if lines[j] == '0':
            start = (i,j)
            lines[j] = '.'
        elif lines[j] == '1':
            ends.append((i,j))
    miro.append(lines)

def isOpen(cur_keys, door):
    return cur_keys & (1<<ord(door)-ord('A'))

def isInbound(x,y):
    return 0<=x<n and 0<=y<m

def bfs(start,ends):
    q = deque()
    q.append((start,0,0))
    visited = [[[0]*(1<<6) for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]][0] = 1
    while q:
        (x,y),cur_key,cnt = q.popleft()
        if (x,y) in ends:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not isInbound(nx,ny) or miro[nx][ny] == '#' or visited[nx][ny][cur_key]:
                continue
            if miro[nx][ny] == '.' or miro[nx][ny] == '1':
                visited[nx][ny][cur_key] = 1
                q.append(((nx,ny),cur_key,cnt+1))
            elif miro[nx][ny].islower():
                new_key = cur_key | (1<<ord(miro[nx][ny])-ord('a'))
                if not visited[nx][ny][new_key]:
                    visited[nx][ny][new_key] = 1
                    q.append(((nx,ny),new_key,cnt+1))
            elif miro[nx][ny].isupper():
                if isOpen(cur_key,miro[nx][ny]):
                    visited[nx][ny][cur_key] = 1
                    q.append(((nx,ny),cur_key,cnt+1))
        
    return -1

print(bfs(start,ends))