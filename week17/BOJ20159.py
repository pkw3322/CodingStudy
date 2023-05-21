import sys

n = int(sys.stdin.readline())
arr = list(map(int,input().split()))
jung = 0
jung1 = 0
jung2 = 0
ans = 0

for i in range(n):
    if i%2 == 0:
        jung += arr[i]
ans = jung
jung1 = jung
for i in range(n-1,0,-2):
    jung1 += arr[i]
    jung1 -= arr[i-1]
    ans = max(ans,jung1)

jung2 = jung
for i in range(n-2,1,-2):
    jung2 += arr[i-1]
    jung2 -= arr[i]
    ans = max(ans,jung2)

print(ans)