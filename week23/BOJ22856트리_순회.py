import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

def total(node):
    global tCount
    visited[node] = True

    if not visited[tree[node][0]] and tree[node][0] != -1:
        total(tree[node][0])
        tCount += 1
    if not visited[tree[node][1]] and tree[node][1] != -1:
        total(tree[node][1])
        tCount += 1

def right(node):
    global rCount
    visited[node] = True
    if not visited[tree[node][1]] and tree[node][1] != -1:
        right(tree[node][1])
        rCount += 1

tree = {}

for _ in range(n):
    a,b,c = map(int,input().split())
    tree[a] = [b,c]
visited = [False]*(n+1)
tCount = 0
total(1)
visited = [False]*(n+1)
rCount = 0
right(1)
print(2*tCount - rCount)