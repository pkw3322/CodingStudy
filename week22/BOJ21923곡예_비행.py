import sys

input = sys.stdin.readline

n,m = map(int,input().split())
vals = [list(map(int,input().split())) for _ in range(n)]

dpUp = [[-sys.maxsize]*m for _ in range(n)]
dpDown = [[-sys.maxsize]*m for _ in range(n)]

dpUp[n-1][0] = vals[n-1][0]
dpDown[n-1][m-1] = vals[n-1][m-1]

for i in range(n-1,-1,-1):
    for j in range(m):
        if i == n-1 and j == 0:
            continue
        if i < n-1 :
            dpUp[i][j] = max(dpUp[i][j],dpUp[i+1][j])
        if j > 0:
            dpUp[i][j] = max(dpUp[i][j],dpUp[i][j-1])
        dpUp[i][j] += vals[i][j]
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if i == n-1 and j == m-1:
            continue
        if i < n-1 :
            dpDown[i][j] = max(dpDown[i][j],dpDown[i+1][j])
        if j < m-1:
            dpDown[i][j] = max(dpDown[i][j],dpDown[i][j+1])
        dpDown[i][j] += vals[i][j]
maxValue = -sys.maxsize
for i in range(n):
    for j in range(m):
        maxValue = max(maxValue,dpUp[i][j]+dpDown[i][j])
print(maxValue)
