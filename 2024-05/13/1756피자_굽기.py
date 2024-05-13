import sys

input = sys.stdin.readline

d,n = map(int,input().split())
ovens = list(map(int,input().split()))
pizzas = list(map(int,input().split()))
idx = 0
oven_idx = d-1

for i in range(len(ovens)-1):
    if ovens[i] < ovens[i+1]:
        ovens[i+1] = ovens[i]

for p in pizzas:
    while oven_idx >= 0:
        if p <= ovens[oven_idx]:
            oven_idx -= 1
            idx += 1
            break
        else:
            oven_idx -= 1


if idx == n:
    print(oven_idx + 2)
else:
    print(oven_idx + 1)
