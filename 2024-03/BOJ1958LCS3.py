str1 = input()
str2 = input()
str3 = input()

n = len(str1)
m = len(str2)
l = len(str3)

dp = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,l+1):
            if str1[i-1] == str2[j-1] and str2[j-1] == str3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else :
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
ans = -1

for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(1,l+1):
            ans = max(ans,dp[i][j][k])
print(ans)