import sys

input = sys.stdin.readline

sdoku = [list(map(int,input().split())) for _ in range(9)]

zeros = []

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zeros.append((i,j))

def check(x,y,num,sdoku):
    for i in range(9):
        if sdoku[x][i] == num or sdoku[i][y] == num:
            return False
    for i in range(x//3*3,x//3*3+3):
        for j in range(y//3*3,y//3*3+3):
            if sdoku[i][j] == num:
                return False
    return True

def dfs(idx,sdoku):
    if idx == len(zeros):
        for row in sdoku:
            print(*row)
        sys.exit()
    x,y = zeros[idx]
    for i in range(1,10):
        if check(x,y,i,sdoku):
            sdoku[x][y] = i
            dfs(idx+1,sdoku)
            sdoku[x][y] = 0

dfs(0,sdoku)
