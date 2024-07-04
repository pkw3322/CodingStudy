import sys
from collections import deque

input = sys.stdin.readline

test = int(input())

def check(from1, from2, to):
    idx = 0
    q = deque()
    q.append((0, 0))
    visited = [[False]*(len(from2)+1) for _ in range(len(from1)+1)]
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == len(from1) and j == len(from2):
                return True
            if i < len(from1) and from1[i] == to[idx] and not visited[i+1][j]:
                q.append((i+1, j))
                visited[i+1][j] = True

            if j < len(from2) and from2[j] == to[idx] and not visited[i][j+1]:
                q.append((i, j+1))
                visited[i][j+1] = True
        idx += 1
    return False

for t in range(test):
    words = input().split()
    from1, from2, to = words[0], words[1], words[2]
    if len(from1) + len(from2) != len(to):
        print('Data set %d: no'% (t+1))
        continue
    if check(from1, from2, to):
        print('Data set %d: yes'% (t+1))
    else:
        print('Data set %d: no'% (t+1))