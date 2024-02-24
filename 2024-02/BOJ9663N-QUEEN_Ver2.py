import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
chess = [0]*n

def isPosible(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(x - i) == abs(chess[x] - chess[i]):
            return False
    return True

def solution(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        chess[x] = i
        if isPosible(x):
            solution(x+1)

solution(0)
print(cnt)