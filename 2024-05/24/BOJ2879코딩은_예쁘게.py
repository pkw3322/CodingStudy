import sys

input = sys.stdin.readline

n = int(input())
curTab = list(map(int,input().split()))
toGoTab = list(map(int,input().split()))
diffs = [toGoTab[i] - curTab[i] for i in range(n)]
dp = [0] * n
dp[0] = abs(diffs[0])

for i in range(1,n):
    if diffs[i]*diffs[i-1] > 0:
        dp[i] = dp[i-1] + max(0,abs(diffs[i]) - abs(diffs[i-1]))
    else:
        dp[i] = dp[i-1] + abs(diffs[i])

print(dp[-1])