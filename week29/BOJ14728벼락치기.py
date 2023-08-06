import sys

input = sys.stdin.readline

n,t = map(int,input().split())

time, score = [0], [0]

for _ in range(n):
    ti,scr = map(int,input().split())
    time.append(ti)
    score.append(scr)

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,t+1):
        if j >= time[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i]] + score[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])