import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort()
dp = []
check = []
els = []
for _,j in arr:
    s = bisect_left(check,j)
    if len(check) != s:
        check[s] = j
    else:
        check.append(j)
    dp.append(s+1)
s = len(check)
print(n-s)
for i in range(len(dp)-1,-1,-1):
    if dp[i] == s:
        s -= 1
    else:
        els.append(arr[i][0])
for i in els[::-1]:
    print(i)