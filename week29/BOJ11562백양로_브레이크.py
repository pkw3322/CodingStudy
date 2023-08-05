import sys

input = sys.stdin.readline

n,m = map(int,input().split())
graphs = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    graphs[i][i] = 0

for _ in range(m):
    u,v,b = map(int, input().split())
    if b == 0:
        graphs[u][v] = 0
        graphs[v][u] = 1
    else:
        graphs[u][v] = 0
        graphs[v][u] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graphs[i][j] = min(graphs[i][j],graphs[i][k] + graphs[k][j])

k = int(input())

for _ in range(k):
    s,e = map(int,input().split())
    print(graphs[s][e])