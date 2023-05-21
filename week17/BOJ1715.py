from heapq import heappush,heappop
import sys

n = int(input())
arr = []

for _ in range(n):
    heappush(arr,int(sys.stdin.readline()))

if len(arr) == 1:
    print(0)
else:
    ans = 0
    while len(arr) > 1:
        tmp1 = heappop(arr)
        tmp2 = heappop(arr)
        ans += (tmp1 + tmp2)
        heappush(arr,tmp1+tmp2)
    print(ans)