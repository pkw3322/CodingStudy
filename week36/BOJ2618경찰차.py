import sys
input = sys.stdin.readline

N = int(input())
W = int(input())
first,second = [[0,0]],[[N-1,N-1]]

for _ in range(W):
    a,b = map(int,input().split())
    first.append([a-1,b-1])
    second.append([a-1,b-1])

dp = [[sys.maxsize for _ in range(W+1)] for _ in range(W+1)]
fromWhere = [[0 for _ in range(W+1)] for _ in range(W+1)]

dp[0][0] = 0
best = []

for i in range(W+1):
    for j in range(W+1):
        if i == j :
            continue
        if i < j :
            if i and j == i+1:
                for k in range(i):
                    if dp[i][j] > dp[i][k] + abs(second[j][0]-second[k][0]) + abs(second[j][1] - second[k][1]):
                        dp[i][j] = dp[i][k] + abs(second[j][0]-second[k][0]) + abs(second[j][1] - second[k][1])
                        fromWhere[i][j] = k
            else:
                dp[i][j] = dp[i][j-1] + abs(second[j][0]-second[j-1][0]) + abs(second[j][1]-second[j-1][1])
                fromWhere[i][j] = j-1
        else:
            if j and i == j+1:
                for k in range(j):
                    if dp[i][j] > dp[k][j]+abs(first[i][0]-first[k][0])+abs(first[i][1]-first[k][1]):
                        dp[i][j] = dp[k][j]+abs(first[i][0]-first[k][0])+abs(first[i][1]-first[k][1])
                        fromWhere[i][j] = k
            else:
                dp[i][j] = dp[i-1][j] + abs(first[i][0] - first[i-1][0]) + abs(first[i][1] - first[i-1][1])
                fromWhere[i][j] = i-1

compare = sys.maxsize
I,J = 0,0
for i in range(W):
    if dp[i][W] < compare:
        I = i
        J = W
        compare = dp[i][W]
    if dp[W][i] < compare:
        I = W
        J = i
        compare = dp[W][i]
print(dp[I][J])
for i in range(W):
    if J > I:
        J = fromWhere[I][J]
        best.append(2)
    else:
        I = fromWhere[I][J]
        best.append(1)

for i in range(W-1,-1,-1):
    print(best[i])
