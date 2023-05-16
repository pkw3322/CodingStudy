import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def mov(pre,next):
    if pre == next:
        return 1
    elif pre == 0:
        return 2
    elif abs(pre-next)%2 == 0:
        return 4
    else:
        return 3

arr = list(map(int,input().split()))
dp = [[[-1]*100000 for _ in range(5)] for _ in range(5)]

def solution(n,left,right):
    global dp

    if n >= len(arr)-1:
        return 0
    if dp[left][right][n] != -1:
        return dp[left][right][n]
    dp[left][right][n] = min(solution(n+1,arr[n],right)+mov(left,arr[n]),solution(n+1,left,arr[n]) + mov(right,arr[n])) 
    return dp[left][right][n]
print(solution(0,0,0))