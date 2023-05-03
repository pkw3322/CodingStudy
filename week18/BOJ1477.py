import sys

N,M,L = map(int,sys.stdin.readline().split())

arr = [0] + list(map(int,sys.stdin.readline().split())) + [L]

arr.sort()

ans = 0

left,right = 1,L-1

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for i in range(1,len(arr)):
        if arr[i] - arr[i-1] > mid :
            cnt += (arr[i] - arr[i-1] - 1)//mid
    if cnt > M:
        left = mid + 1
    else :
        right = mid - 1
        ans = mid

print(ans)