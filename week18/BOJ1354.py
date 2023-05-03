from collections import defaultdict
import sys

N,P,Q,X,Y = map(int,sys.stdin.readline().split())

dp = defaultdict(int)
dp[0] = 1

def func(n):
    if n <= 0:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = func(int(n/P)-X) + func(int(n/Q)-Y)
    return dp[n]

print(func(N))