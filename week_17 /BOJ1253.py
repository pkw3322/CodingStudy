import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
ans = 0

for i in range(n):
    tmpArr = arr[:i] + arr[i+1:]
    left,right = 0,len(tmpArr)-1
    while left < right:
        temp = tmpArr[left] + tmpArr[right]
        if temp == arr[i]:
            ans += 1
            break
        if temp < arr[i]:
            left += 1
        else :
            right -= 1

print(ans)
