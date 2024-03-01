import sys

input = sys.stdin.readline

def func(n, arr):
    rev = arr[::-1]
    increase = [1 for _ in range(n)]
    decrease = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                increase[i] = max(increase[i],increase[j] + 1)
            if rev[i] > rev[j]:
                decrease[i] = max(decrease[i],decrease[j] + 1)
    result = [increase[i] + decrease[n - i - 1] - 1 for i in range(n)]
    
    return max(result)

n = int(input())
arr = list(map(int,input().split()))

print(func(n,arr))