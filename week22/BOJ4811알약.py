import sys

input = sys.stdin.readline
dp = [[0]*31 for _ in range(31)]
for i in range(31):
    dp[0][i] = 1
while True:
    n = int(input())
    if n == 0:
        break
    if dp[n][n] != 0:
        print(dp[n][n])
    else :
        for i in range(1,n+1):
            for j in range(i,n+1):
                if dp[i][j] != 0:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp[n][n])
                
            
