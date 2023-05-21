from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N,P,Q = map(int,sys.stdin.readline().split())

dp = defaultdict(int)

dp[0] = 1

def func(n):
    if dp[n] != 0 : 
        return dp[n]
    dp[n] = func(int(n/P)) + func(int(n/Q))

    return dp[n]

print(func(N))
