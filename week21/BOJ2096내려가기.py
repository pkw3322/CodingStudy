import sys
input = sys.stdin.readline

n = int(input())
minDp = [0,0,0]
maxDp = [0,0,0]
minTemp = [0,0,0]
maxTemp = [0,0,0]

for i in range(n):
    a,b,c = map(int,input().split())
    minTemp[0] = a + min(minDp[0],minDp[1])
    maxTemp[0] = a + max(maxDp[0],maxDp[1])
    minTemp[1] = b + min(minDp)
    maxTemp[1] = b + max(maxDp)
    minTemp[2] = c + min(minDp[1],minDp[2])
    maxTemp[2] = c + max(maxDp[1],maxDp[2])
    for j in range(3):
        maxDp[j] = maxTemp[j]
        minDp[j] = minTemp[j]
print(max(maxDp),min(minDp))