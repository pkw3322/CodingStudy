import sys

input = sys.stdin.readline
def bisect(start,end,arr,c):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == c:
            return True
        elif arr[mid] < c:
            start = mid+1
        else:
            end = mid-1
    return False

def func(n,c,arr):
    if c in arr:
        return True
    start = 0
    end = n-1
    while start < end:
        Sum = arr[start] + arr[end]
        if Sum > c:
            end -= 1
        elif Sum == c:
            return True
        else:
            dif = c - Sum
            if arr[start] != dif and arr[end] != dif and bisect(start,end,arr,dif):
                return True
            start += 1

n,c = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

if func(n,c,arr):
    print(1)
else:
    print(0)