import sys

input = sys.stdin.readline

def dp(cur):
    child = []
    for i in tree[cur]:
        dp(i)
        child.append(visited[i])
    if not tree[cur]:
        child.append(0)
    child.sort(reverse=True)

    needs = [child[i]+i+1 for i in range(len(child))]
    visited[cur] = max(needs)

n = int(input())
arr = list(map(int,input().split()))
tree = [[] for _ in range(n)]

for i in range(1,n):
    tree[arr[i]].append(i)

visited = [False for _ in range(n)]

dp(0)
print(visited[0]-1)
