import sys

input = sys.stdin.readline

n = int(input())
nArr = list(map(int,input().split()))

m = int(input())
mArr = list(map(int,input().split()))

dp = [0]
for weight in nArr:
    temp = []
    for i in dp:
        temp.append(i+weight)
        temp.append(abs(i-weight))
    dp = list(set(dp + temp))

for i in mArr:
    print('Y' if i in dp else 'N',end = ' ')
    