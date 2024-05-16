import sys

input = sys.stdin.readline

bs = list(map(int,input().split()))

balls = []

for i in range(5):
    a,b = map(int,input().split())
    balls.append((a,b))

dp = [[-1]*501 for _ in range(501)]

def check(a,b):
    if dp[a][b] >= 0:
        return dp[a][b]
    for i in range(3):
        if a >= bs[i] and not check(a-bs[i],b):
            dp[a][b] = 1
            return dp[a][b]
    for i in range(3):
        if b >= bs[i] and not check(a,b-bs[i]):
            dp[a][b] = 1
            return dp[a][b]
    dp[a][b] = 0

    return dp[a][b]

for a,b in balls:
    temp = check(a,b)
    if temp == 1:
        print("A")
    else:
        print("B")
