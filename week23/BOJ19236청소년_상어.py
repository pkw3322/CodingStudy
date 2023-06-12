import sys
import copy
input = sys.stdin.readline

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
board = [[(0,0)]*4 for _ in range(4)]

for i in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int,input().split())
    board[i][0] = [a1,b1-1]
    board[i][1] = [a2,b2-1]
    board[i][2] = [a3,b3-1]
    board[i][3] = [a4,b4-1]

ans = 0
def dfs(shax,shay,score,board):
    global ans
    score += board[shax][shay][0]
    ans = max(ans,score)
    board[shax][shay][0] = 0

    for f in range(1,17):
        fx,fy = -1,-1
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == f:
                    fx = i
                    fy = j
                    break
        
        if fx == -1 and fy == -1:
            continue

        fd = board[fx][fy][1]
        for i in range(fd,fd+8):
            nd = i%8
            nx = fx + dx[nd]
            ny = fy + dy[nd]
            if 0<=nx<4 and 0<=ny<4:
                if nx == shax and ny == shay:
                    continue
                board[fx][fy][1] = nd
                temp = board[fx][fy]
                board[fx][fy] = board[nx][ny]
                board[nx][ny] = temp
                break

    sd = board[shax][shay][1]
    for i in range(1,5):
        nx = shax + dx[sd]*i
        ny = shay + dy[sd]*i
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0] > 0:
            dfs(nx,ny,score,copy.deepcopy(board))
    

dfs(0,0,0,board)
print(ans)