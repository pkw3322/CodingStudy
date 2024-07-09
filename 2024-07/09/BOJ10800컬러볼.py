import sys

input = sys.stdin.readline

n = int(input())
arr = [(0,0,0)]
balls = [0]*(2001)
colors = [0]*(n+1)
ans = [0]* (n+1)
for i in range(1,n+1):
    c,s = map(int,input().split())
    arr.append((s,c,i))
arr.sort()

sums = [0]*(n+1)

for i in range(1,n+1):
    sums[i] = sums[i-1] + arr[i][0]
    if arr[i][1] == arr[i-1][1] and arr[i][0] == arr[i-1][0]:
        ans[arr[i][2]] = ans[arr[i-1][2]]
    else:
        ans[arr[i][2]] = sums[i-1] - balls[arr[i][0]] - colors[arr[i][1]]
    balls[arr[i][0]] += arr[i][0]
    colors[arr[i][1]] += arr[i][0]

for i in range(1,n+1):
    print(ans[i])