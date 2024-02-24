import sys

input = sys.stdin.readline

n,c = map(int,input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

def binarySearch(start,end,arr):
    global answer
    while start <= end:
        mid = (start + end) // 2
        cur = arr[0]
        cnt = 1

        for i in range(1,len(arr)):
            if arr[i] >= cur + mid:
                cnt += 1
                cur = arr[i]
        if cnt >= c:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
start = 1
end = arr[-1] - arr[0]
answer = 0

binarySearch(start,end, arr)
print(answer)