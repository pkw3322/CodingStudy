import sys

input = sys.stdin.readline

n,m = map(int,input().split())

conti = [[0]+[-1e7]*m for _ in range(n+1)]
notConti = [[0]+[-1e7]*m for _ in range(n+1)]

for i in range(1,n+1):
    num = int(input())
    for j in range(1,min(m,(i+1)//2)+1):
        notConti[i][j] = max(notConti[i-1][j],conti[i-1][j])
        conti[i][j] = max(notConti[i-1][j-1],conti[i-1][j])+num

print(max(conti[n][m],notConti[n][m]))