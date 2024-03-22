import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

arr.sort()

left = 0
right = n-1
result = (0,0)
total_diff = sys.maxsize

while left < right:
    diff = arr[right] + arr[left]
    if abs(diff) < total_diff:
        total_diff = abs(diff)
        result = (arr[left],arr[right])
    if diff < 0:
        left += 1
    else:
        right -= 1

print(result[0],result[1])