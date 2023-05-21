import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())


def dfs(start):
    global res
    visited[start] = True
    addList.append(start)

    if visited[numList[start]]:
        if numList[start] in addList :
            res -= len(addList[addList.index(numList[start]):])
        return
    else:
        dfs(numList[start])
        
for _ in range(t):
    n = int(input())
    numList = [0] + list(map(int,input().split()))
    visited = [False]*(n+1)
    res = n
    for i in range(1,n+1):
        if not visited[i]:
            addList = []
            dfs(i)
    print(res)
    