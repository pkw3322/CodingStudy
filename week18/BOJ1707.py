import sys
sys.setrecursionlimit(10**6)
test = int(input())

def dfs(start,group):
    visited[start] = group

    for i in graph[start]:
        if not visited[i]:
            a = dfs(i,-group)
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for _ in range(test):
    v,e = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    for _ in range(e):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if not visited[i]:
            result = dfs(i,1)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")