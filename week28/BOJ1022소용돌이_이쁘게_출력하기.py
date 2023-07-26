import sys

input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]

r1,c1,r2,c2 = map(int,input().split())
h = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

total = (c2-c1+1) * (r2-r1+1)
d = 0
cx = 0
cy = 0
cnt = 0
num = 1
line = 1

while total > 0:
    if r1 <= cx <= r2 and c1 <= cy <= c2:
        total -= 1
        h[cx-r1][cy-c1] = num
        m = num
    num += 1
    cnt += 1

    cx += dx[d]
    cy += dy[d]

    if cnt == line:
        cnt = 0
        d = (d+1)%4
        if d == 0 or d == 2:
            line += 1

max_len = len(str(m))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(h[i][j]).rjust(max_len), end=" ")
    print()