n = int(input())
k = int(input())

start,end = 1,k
while start <= end:
    mid = (start + end) // 2

    tem = 0
    for i in range(1,n+1):
        tem += min(mid//i,n)
    if tem >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)