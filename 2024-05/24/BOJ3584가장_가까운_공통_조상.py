import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    trees = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        trees[b].append(a)
    x,y = map(int,input().split())
    px = []
    py = []
    def dfs(cur,path):
        if trees[cur] == []:
            return path
        for nxt in trees[cur]:
            path.extend(dfs(nxt,[nxt]))
        return path
    px = dfs(x,[x])
    py = dfs(y,[y])
    for i in px:
        for j in py:
            if i == j:
                print(i)
                break
        if i == j:
            break

