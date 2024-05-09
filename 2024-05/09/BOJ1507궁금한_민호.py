import sys

input = sys.stdin.readline

n = int(input())

roads = [list(map(int, input().split())) for _ in range(n)]
basic = {}

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k:
                continue
            if roads[i][j] > roads[i][k] + roads[k][j]:
                print(-1)
                sys.exit()
            if roads[i][j] == roads[i][k] + roads[k][j]:
                basic[(i, j)] = 1

total_sum = 0
for i in range(n):
    for j in range(n):
        total_sum += roads[i][j]

not_basic = 0
for k in basic.keys():
    not_basic += roads[k[0]][k[1]]

print((total_sum - not_basic)//2)
