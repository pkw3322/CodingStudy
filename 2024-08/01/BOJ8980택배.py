import sys

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
boxCost = [list(map(int, input().split())) for _ in range(m)]

boxCost.sort(key=lambda x: (x[1], x[0], -x[2]))

truck = [c] * (n+1)
total = 0

for i in range(m):
    minBox = min(truck[boxCost[i][0]:boxCost[i][1]])
    if minBox >= boxCost[i][2]:
        total += boxCost[i][2]
        for j in range(boxCost[i][0], boxCost[i][1]):
            truck[j] -= boxCost[i][2]
    else:
        total += minBox
        for j in range(boxCost[i][0], boxCost[i][1]):
            truck[j] -= minBox
    
print(total)