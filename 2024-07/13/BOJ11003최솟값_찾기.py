import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
numbers = list(map(int, input().split()))
minList = []
q = deque()

for i in range(n):
    while q and q[-1][1] > numbers[i]:
        q.pop()
    q.append((i, numbers[i]))
    if q[0][0] <= i - l:
        q.popleft()
    minList.append(q[0][1])

print(*minList)