import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for i in range(1,n):
    if board[0][i] == 1:
        break
    else:
        dp[0][i][0] = 1

for i in range(1,n):
    for j in range(2,n):
        if not board[i][j]:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if not board[i-1][j] and not board[i][j-1] and not board[i][j]:
            dp[i][j][2] = sum(dp[i-1][j-1])
    

print(sum(dp[n-1][n-1]))