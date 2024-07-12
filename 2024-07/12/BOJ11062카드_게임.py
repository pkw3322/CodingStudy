import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    points =list(map(int,input().split()))
    
    turn = 0 if n % 2 == 0 else 1
    dp = [[0]*n for _ in range(n)]
    
    for length in range(n):
        for i in range(n-length):
            if length == 0:
                if turn:
                    dp[i][i] = points[i]
                else :
                    dp[i][i] = 0
            elif turn:
                dp[i][i+length] = max(dp[i+1][i+length] + points[i], dp[i][i+length-1] + points[i+length])
            else:
                dp[i][i+length] = min(dp[i+1][i+length], dp[i][i+length-1])
        turn = 1 - turn

    print(dp[0][n-1])
