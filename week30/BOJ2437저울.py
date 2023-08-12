import sys

input = sys.stdin.readline

n = int(input())
weights = list(map(int,input().split()))
weights.sort()
possible = [(0,0)]

for weight in weights:
    a,b = possible[-1]
    if b + 1 >= a + weight:
        possible.append((a,b+weight))
    else:
        possible.append((a+weight,b+weight))
for i in range(len(possible)):
    start,end = possible[i]
    if start != 0:
        _,max = possible[i-1]
        print(max+1)
        exit(0)
_,end = possible[-1]
print(end+1)