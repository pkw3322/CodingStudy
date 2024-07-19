import sys

input = sys.stdin.readline

n = int(input())
drawings = [list(map(int, input().rstrip())) for _ in range(n)]

dp = [[[0]*10 for _ in range(n)] for _ in range(1<<n)]

def dfs(idx, artist, cost):
    if dp[idx][artist][cost]:
        return dp[idx][artist][cost]
    cnt = 0
    for i in range(1,n):
        if drawings[artist][i] >= cost and idx&(1<<i) <= 0:
            cnt = max(cnt, dfs(idx|(1<<i), i, drawings[artist][i]) + 1)
    dp[idx][artist][cost] = cnt

    return cnt

print(dfs(1,0,0)+1)