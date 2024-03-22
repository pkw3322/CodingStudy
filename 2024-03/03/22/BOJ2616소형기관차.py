import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
k = int(input())

totals = [0]
temp = 0
for i in arr:
    temp += i
    totals.append(temp)

dp = [[0 for _ in range(n+1)] for _ in range(4)]

for num in range(1,4):
    for cur in range(num*k,n+1):
        if num == 1:
            dp[num][cur] = max(dp[num][cur-1],totals[cur] - totals[cur-k])
        else:
            dp[num][cur] = max(dp[num-1][cur-k] + totals[cur] - totals[cur-k], dp[num][cur-1])


print(dp[3][n])