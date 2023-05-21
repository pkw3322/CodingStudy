import sys

input = sys.stdin.readline

n = int(input())
ans = 0.0
x = []
y = []
for _ in range(n):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)
tx,ty = 0,0
for i in range(n):
    tx += x[i]*y[(i+1)%n]
    ty += y[i]*x[(i+1)%n]

print(round(abs((tx-ty)/2),1))