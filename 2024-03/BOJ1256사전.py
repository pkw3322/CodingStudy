import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

dp = [[1]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[n][m] < k:
    print('-1')
else:
    ans = ""
    while n > 0 and m > 0:
        s = dp[n-1][m]
        if k <= s:
            n -= 1
            ans += "a"
        else :
            m -= 1
            ans += "z"
            k -= s
    ans += ("a"*n + "z"*m)
    print(ans)
