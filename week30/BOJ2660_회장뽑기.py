import sys

input = sys.stdin.readline

n = int(input())
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] == 1 or graph[i][j] == 0:
                continue
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

res = []
for i in range(1,n+1):
    res.append(max(graph[i][1:]))

ans = min(res)
print(ans, res.count(ans))

for i in range(len(res)):
    if ans == res[i]:
        print(i+1, end = " ")