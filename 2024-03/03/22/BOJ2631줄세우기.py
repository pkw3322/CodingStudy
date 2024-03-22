n = int(input())
lines = [0] + [int(input()) for _ in range(n)]
dp = [1 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i):
        if lines[i] > lines[j]:
            dp[i] = max(dp[j]+1,dp[i])

print(n - max(dp))