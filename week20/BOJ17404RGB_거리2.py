import sys
input = sys.stdin.readline

n = int(input())
rgbs = []

for _ in range(n):
    rgb = list(map(int,input().split()))
    rgbs.append(rgb)
ans = sys.maxsize

for i in range(3):
    dp = [[sys.maxsize]*3 for _ in range(n)]
    dp[0][i] = rgbs[0][i]
    for j in range(1,n):
        dp[j][0] = rgbs[j][0] + min(dp[j-1][1],dp[j-1][2])
        dp[j][1] = rgbs[j][1] + min(dp[j-1][0],dp[j-1][2])
        dp[j][2] = rgbs[j][2] + min(dp[j-1][0],dp[j-1][1])
    for j in range(3):
        if i != j:
            ans = min(ans,dp[n-1][j])

print(ans)