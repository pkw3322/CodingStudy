import sys

input = sys.stdin.readline
ans = 0

def dfs(x,y):
    if y == c-1:
        return True
    for dx in [-1,0,1]:
        nx = x + dx
        ny = y + 1
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] != 'x' and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                if dfs(nx,ny):
                    return True
    
    return False


r,c = map(int,input().split())
visited = [[-1 for _ in range(c)] for _ in range(r)]
board = [list(input().strip()) for _ in range(r)]

for i in range(r):
    if dfs(i,0):
        ans += 1

print(ans)