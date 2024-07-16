import sys

input = sys.stdin.readline

def find(v):
    if parents[v] == v:
        return v
    parents[v] = find(parents[v])
    return parents[v]

def union(v1,v2):
    r1 = find(v1)
    r2 = find(v2)
    if r1 < r2:
        r1,r2 = r2,r1
    parents[r1] = r2

n,m,k = map(int,input().split())
candies = [0] + list(map(int,input().split()))
parents = [i for i in range(n+1)]
friendCount = [1]*(n+1)
dp = [0 for _ in range(k)]

for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

for i in range(1,n+1):
    if i != parents[i]:
        root = find(i)
        candies[root] += candies[i]
        friendCount[root] += friendCount[i]

for i in range(1,n+1):
    if i != parents[i]:
        continue
    for j in range(k-1, friendCount[i]-1, -1):
        dp[j] = max(dp[j], dp[j-friendCount[i]] + candies[i])

print(max(dp))
