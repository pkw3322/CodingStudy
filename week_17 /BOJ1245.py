import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]
    global flag
    Visit[x][y] = True

    for i in range(8): 
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < N and -1 < ny < M:
            if mountain[x][y] < mountain[nx][ny]:
                flag = False
            if not Visit[nx][ny] and mountain[x][y] == mountain[nx][ny]:
                dfs(nx,ny)


N,M = map(int,input().split())
mountain = [list(map(int,input().split())) for _ in range(N)]
Visit = [[False]*M for _ in range(N)]
flag = True
cnt = 0

for i in range(N):
    for j in range(M):
        if not Visit[i][j] and mountain[i][j] > 0 : 
            flag = True
            dfs(i,j)

            if flag : 
                cnt += 1

print(cnt)