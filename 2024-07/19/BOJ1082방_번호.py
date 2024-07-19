import sys

input = sys.stdin.readline

n = int(input())
prices = list(map(int, input().split()))
m = int(input())

dp = [0] * (m+1)

for i in range(n-1,-1,-1):
    x = prices[i]
    for j in range(x,m+1):
        dp[j] = max(dp[j], dp[j-x]*10 + i)

print(dp[m])