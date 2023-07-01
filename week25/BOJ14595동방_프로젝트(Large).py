import sys
from collections import defaultdict

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    temp = find(parent[x])
    parent[x] = temp
    return temp

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
ranges = defaultdict(list)
for i in range(1,n+1):
    ranges[i] = [i,i]

for _ in range(m):
    a,b = map(int,input().split())
    pa = find(a)
    pb = find(b)

    if pa == pb:
        continue

    update, start, end = 0, 0, 0
    if pa < pb:
       start = pa
       end = pb
       update = pa
    else:
        start = pb
        end = pa
        update = pb

    idx = start

    while idx <= end:
        parent[idx] = update
        s, e = ranges[idx]
        idx = e + 1

    ranges[update] = [a, b]

ans = set()

for i in range(1,n+1):
    ans.add(find(parent[i]))

print(len(ans))