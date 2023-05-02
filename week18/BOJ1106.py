c,n = map(int,input().split())

cost_list = [list(map(int,input().split())) for _ in range(n)]

dp = [10000000 for _ in range(c+100)]

dp[0] = 0

for cost,people in cost_list:
    for i in range(people,len(dp)):
        dp[i] = min(dp[i-people] + cost,dp[i])

print(min(dp[c:]))
