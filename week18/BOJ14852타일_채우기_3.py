import sys

input = sys.stdin.readline

n = int(input())
mod = 1000000007
dp = [0]*(n+1)
sum_arr = [0]*(n+1)
if n == 1:
    print (2)
    sys.exit()
elif n == 2:
    print(7)
    sys.exit()
dp[0] = 1
dp[1] = 2
dp[2] = 7
sum_arr[0] = 1
sum_arr[1] = 3
sum_arr[2] = 10
for i in range(3,n+1):
    dp[i] = (sum_arr[i-1]*2 + dp[i-2])%mod
    sum_arr[i] = (sum_arr[i-1] + dp[i])%mod
    
print(dp[n])