import sys

input = sys.stdin.readline

str1 = " " + input().strip()
str2 = " " + input().strip()
n,m = len(str1)-1,len(str2)-1
dp = [[0]*(m+1) for _ in range(n+1)]
back = [[0]*(m+1) for _ in range(n+1)]
def getLCS(arr,n,m):
    i,j = n,m
    ans = ""
    while i > 0 and j > 0:
        if arr[i][j] == 1:
            ans += str1[i]
            i -= 1
            j -= 1
        elif arr[i][j] == 2:
            i -= 1
        else :
            j -= 1
    
    return ans[::-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            back[i][j] = 1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if dp[i-1][j] > dp[i][j-1] : 
                back[i][j] = 2
            else :
                back[i][j] = 3

print(dp[n][m])
print(getLCS(back,n,m))