import sys

input = sys.stdin.readline

def func(n,m,arr):
    mod = [0 for _ in range(m)]
    prefixSum = 0
    for i in range(n):
        prefixSum += arr[i]
        mod[prefixSum%m] += 1
    ans = mod[0]
    for i in range(m):
        ans += mod[i]*(mod[i] - 1)//2
    return ans

n,m = map(int,input().split())

arr = list(map(int,input().split()))

print(func(n,m,arr))