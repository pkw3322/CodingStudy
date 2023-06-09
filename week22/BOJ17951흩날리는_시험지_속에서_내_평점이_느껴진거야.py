import sys

input = sys.stdin.readline

n,k = map(int,input().split())
probs = list(map(int,input().split()))
ans = 0
start,end = 0,(10**5)*20 + 1

while start <= end:
    mid = (start+end)//2
    totalGroup = 0
    curScore = 0
    for p in probs:
        curScore += p
        if curScore >= mid:
            totalGroup += 1
            curScore = 0
    
    if totalGroup >= k:
        ans = mid
        start = mid+1
    else:
        end = mid - 1
print(ans)