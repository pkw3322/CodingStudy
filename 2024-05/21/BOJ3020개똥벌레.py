import sys

input = sys.stdin.readline

n,h = map(int,input().split())

lines = [0]*(h)

for i in range(n):
    a = int(input())
    if i%2 == 0:
        lines[h-a] += 1
    else:
        lines[0] += 1
        lines[a] -= 1

for i in range(1,h):
    lines[i] += lines[i-1]

result = 0
min_value = min(lines)

for l in lines:
	if l == min_value:
          result += 1

print(min_value, result)
