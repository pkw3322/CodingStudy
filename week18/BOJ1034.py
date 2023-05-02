import sys

N,M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(input())

K = int(input())

maxCount = 0

for i in range(N):
    zeros = 0
    for num in arr[i]:
        if num == '0':
            zeros += 1
    
    curCount = 0
    if zeros <= K and zeros%2 == K%2:
        for col in range(N):
            if arr[col] == arr[i]:
                curCount += 1
    maxCount = max(maxCount,curCount)

print(maxCount)