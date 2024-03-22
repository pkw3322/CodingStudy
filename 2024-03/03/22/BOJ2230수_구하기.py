import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [int(input()) for _ in range(n)]

arr.sort()

left = 0
right = 0
answer = sys.maxsize

while left < n and right < n:
    diff = arr[right] - arr[left]
    if diff >= m:
        answer = min(answer,diff)
        left += 1
    else:
        right += 1
print(answer)