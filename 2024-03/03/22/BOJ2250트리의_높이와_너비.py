import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

trees = [[-1,-1,-1] for _ in range(n+1)]

for _ in range(n):
    cur,left,right = map(int,input().split())
    trees[cur][1] = left
    trees[cur][2] = right
    trees[left][0] = cur
    trees[right][0] = cur

root = -1

for i in range(1,n+1):
    if trees[i][0] == -1:
        root = i

visited = [[-1,-1] for _ in range(n+1)]

def bfs(root):
    depth = 0
    q = deque()
    q.append(root)
    visited[root][0] = 0
    while q:
        cur = q.popleft()
        left = trees[cur][1]
        right = trees[cur][2]
        if left != -1:
            if visited[left][0] == -1:
                visited[left][0] = visited[cur][0] + 1
                depth = max(depth,visited[left][0])
                q.append(left)
        if right != -1:
            if visited[right][0] == -1:
                visited[right][0] = visited[cur][0] + 1
                depth = max(depth,visited[right][0])
                q.append(right)
    return depth

distance = 0

def inorder_search(x):
    global distance
    if trees[x][1] != -1:
        inorder_search(trees[x][1])
    
    distance += 1
    visited[x][1] = distance

    if trees[x][2] != -1:
        inorder_search(trees[x][2])

max_depth = bfs(root)
inorder_search(root)

max_distance = 0
min_level = sys.maxsize

if n == 1:
    print(1,1)
else: 
    for dep in range(max_depth+1):
        min_val = sys.maxsize
        max_val = 0
        for i in range(1,n+1):
            if visited[i][0] == dep:
                min_val = min(visited[i][1],min_val)
                max_val = max(visited[i][1],max_val)
        if max_distance < max_val - min_val + 1:
            max_distance = max_val - min_val + 1
            min_level = dep + 1

    print(min_level,max_distance)
