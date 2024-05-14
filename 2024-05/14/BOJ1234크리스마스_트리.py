import sys
import math
input = sys.stdin.readline

n, r, g, b = map(int, input().split())

totals = n*(n+1)//2
if r + g + b < totals:
    print(0)
    exit()

dp = [[[[0]*101 for _ in range(101)] for _ in range(101)] for _ in range(11)]


def solve(n, r, g, b):
    if n == 0:
        return 1
    if dp[n][r][g][b] != 0:
        return dp[n][r][g][b]
    
    if r >= n:
        dp[n][r][g][b] += solve(n-1, r-n, g, b)
    if g >= n:
        dp[n][r][g][b] += solve(n-1, r, g-n, b)
    if b >= n:
        dp[n][r][g][b] += solve(n-1, r, g, b-n)
    if n % 2 == 0:
        temp = n//2
        toMulti = math.comb(n, temp)
        if r >= temp and g >= temp:
            dp[n][r][g][b] += solve(n-1, r-temp, g-temp, b)*toMulti
        if r >= temp and b >= temp:
            dp[n][r][g][b] += solve(n-1, r-temp, g, b-temp)*toMulti
        if g >= temp and b >= temp:
            dp[n][r][g][b] += solve(n-1, r, g-temp, b-temp)*toMulti
    if n % 3 == 0:
        temp = n//3
        toMulti = math.comb(n, temp)*math.comb(n-temp, temp)
        if r >= temp and g >= temp and b >= temp:
            dp[n][r][g][b] += solve(n-1, r-temp, g-temp, b-temp)*toMulti
    return dp[n][r][g][b]


print(solve(n, r, g, b))
