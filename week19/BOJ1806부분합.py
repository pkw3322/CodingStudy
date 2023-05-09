import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
start,end = 0,0
total = 0
minLength = sys.maxsize

while True:
    if total >= m:
        minLength = min(minLength,end - start)
        total -= arr[start]
        start += 1
    elif end == n:
        break
    else :
        total += arr[end]
        end += 1

if minLength == sys.maxsize:
    print(0)
else :
    print(minLength)