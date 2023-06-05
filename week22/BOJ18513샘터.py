import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
sam = list(map(int,input().split()))
sam.sort()

visited = set()
q = deque()
for s in sam:
    q.append((s,1))
    visited.add(s)
ans = 0
tcnt = 0
flag = True
while q and flag:
    cur,d = q.popleft()
    for i in [-1,1]:
        next = cur + i
        if not next in visited:
            visited.add(next)
            ans += d
            tcnt += 1
            q.append((next,d+1))
            if tcnt == k:
                flag = False
                break
print (ans)