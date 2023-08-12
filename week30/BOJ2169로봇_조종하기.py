import sys

input = sys.stdin.readline

dx = [0,0,1]
dy = [1,-1,0]

n,m = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,m):
    dp[0][i] += dp[0][i-1]

for i in range(1,n):
    toLeft = dp[i][:]
    toRight = dp[i][:]

    for j in range(m):
        if j == 0:
            toLeft[j] += dp[i-1][j]
        else:
            toLeft[j] += max(dp[i-1][j],toLeft[j-1])
    
    for j in range(m-1, -1, -1):
        if j == m-1:
            toRight[j] += dp[i-1][j]
        else:
            toRight[j] += max(dp[i-1][j],toRight[j+1])
    
    for j in range(m):
        dp[i][j] = max(toLeft[j], toRight[j])
print(dp[n-1][m-1])