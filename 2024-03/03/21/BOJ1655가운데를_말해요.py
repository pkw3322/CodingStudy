from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())
max_h = []
min_h = []
ans = []
for i in range(n):
    cur = int(input())
    if len(max_h) == len(min_h):
        heappush(max_h, (-cur, cur))
    else:
        heappush(min_h, (cur, cur))

    if min_h and max_h[0][1] > min_h[0][1]:
        max_value = heappop(max_h)[1]
        min_value = heappop(min_h)[1]
        heappush(max_h, (-min_value, min_value))
        heappush(min_h, (max_value, max_value))
        
    ans.append(max_h[0][1])
print('\n'.join(map(str, ans)))