import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
degree = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    degree[b] += 1

def topology_sort():
    res = []
    q = deque()
    for i in range(1,n+1):
        if degree[i] == 0:
            q.append(i)
    
    while q:
        cur = q.popleft()
        res.append(cur)

        for i in arr[cur]:
            degree[i] -= 1
            
            if degree[i] == 0:
                q.append(i)
    
    for i in res:
        print(i,end = ' ')
topology_sort()
