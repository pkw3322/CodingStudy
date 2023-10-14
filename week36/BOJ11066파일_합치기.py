import sys
input = sys.stdin.readline

testCase = int(input())

for _ in range(testCase):
    n = int(input())
    chapters = [0] + list(map(int,input().split()))
    sumList = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        sumList[i] = sumList[i-1] + chapters[i]
    dp = [[0]*(n+1) for i in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,n+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) + (sumList[j+i-1] - sumList[j-1])

    print(dp[1][n])