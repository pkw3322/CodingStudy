import sys

input = sys.stdin.readline

dx = [0,0,1,-1,0]
dy = [1,-1,0,0,0]

n = int(input())
cy,cx = map(int,input().split())
toGo = [(cx,cy)]

for _ in range(n):
    y,x = map(int,input().split())
    toGo.append((x,y))

dist = [[sys.maxsize]*5 for _ in range(n+1)]
dist[0] = [1]*5
dist[0][4] = 0

for i in range(1,n+1):
    for j in range(5):
        nx = toGo[i][0] + dx[j]
        ny = toGo[i][1] + dy[j]
        for k in range(5):
            cx = toGo[i-1][0] + dx[k]
            cy = toGo[i-1][1] + dy[k]
            dist[i][j] = min(dist[i][j], dist[i-1][k] + abs(nx-cx) + abs(ny-cy))

print(min(dist[n]))