from sys import maxsize

def solution(target):
    dp = [[target-i, target-i] for i in range(target+1)]
    
    for i in range(target, -1, -1):
        if i - 50 >= 0:
            if dp[i-50][0] > dp[i][0] + 1:
                dp[i-50] = [dp[i][0]+1,dp[i][1]+1]
            elif dp[i-50][0] == dp[i][0] + 1 and dp[i-50][1] < dp[i][1] + 1:
                dp[i-50][1] = dp[i][1] + 1
                
        for j in range(20, 0, -1):
            if i - j >= 0:
                if dp[i-j][0] > dp[i][0] + 1:
                    dp[i-j] = [dp[i][0]+1,dp[i][1]+1]
                elif dp[i-j][0] == dp[i][0] + 1 and dp[i-j][1] < dp[i][1] + 1:
                    dp[i-j][1] = dp[i][1] + 1
            else:
                break
                
            if i-2*j >= 0:
                if dp[i-2*j][0] > dp[i][0]+1:
                    dp[i-2*j] = [dp[i][0]+1, dp[i][1]]
                elif dp[i-2*j][0] == dp[i][0]+1 and dp[i-2*j][1] < dp[i][1]:
                    dp[i-2*j] = [dp[i][0]+1, dp[i][1]]
                    
            if i-3*j >= 0:
                if dp[i-3*j][0] > dp[i][0]+1:
                    dp[i-3*j] = [dp[i][0]+1, dp[i][1]]
                elif dp[i-3*j][0] == dp[i][0]+1 and dp[i-3*j][1] < dp[i][1]:
                    dp[i-3*j] = [dp[i][0]+1, dp[i][1]]
    
    return dp[0]