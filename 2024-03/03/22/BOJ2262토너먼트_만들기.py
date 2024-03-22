import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
sorted_arr = sorted(arr, reverse=True)

ans = 0

for i in sorted_arr[:-1]:
    idx = arr.index(i)
    if idx == 0:
        ans += abs(i - arr[idx+1])
    elif idx == len(arr) - 1:
        ans += abs(i - arr[idx-1])
    else:
        ans += min(abs(i - arr[idx-1]), abs(i - arr[idx+1]))
    arr.pop(idx)

print(ans)