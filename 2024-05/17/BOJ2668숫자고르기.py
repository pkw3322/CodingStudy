import sys

input = sys.stdin.readline

n = int(input())

seconds = [int(input())-1 for _ in range(n)]

def check(idxs):
    idxs.sort()
    tem = []
    for i in idxs:
        tem.append(seconds[i])
    tem.sort()
    if tem == idxs:
        return 1
    return 0

def dfs(idx,visited,idxs):
    if visited[idx]:
        if idx in idxs:
            return check(idxs)
        return 0
    visited[idx] = 1
    idxs.append(idx)
    return dfs(seconds[idx],visited,idxs)

answer = 0
ans = []
for i in range(n):
    visited = [0]*n
    if dfs(i,visited,[]):
        answer += 1
        ans.append(i+1)
        
print(answer)
print("\n".join(map(str,ans)))