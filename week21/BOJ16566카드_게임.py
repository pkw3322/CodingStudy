import sys
import math
input = sys.stdin.readline

n,m,k = map(int,input().split())
cards = list(map(int,input().split()))

chuls = list(map(int,input().split()))
sqrtN = int(math.sqrt(n))

visited = [0]*(n+1)
dummy = [0]*(sqrtN+1)
for c in cards:
    visited[c] += 1
    dummy[c//sqrtN] += 1

for chul in chuls:
    cur = chul + 1
    while dummy[cur//sqrtN] == 0 and cur <= n:
        cur = ((cur//sqrtN)+1)*sqrtN
    if cur > n:
        cur = 0
        while dummy[cur//sqrtN] == 0 and cur <= n:
            cur = ((cur//sqrtN)+1)*sqrtN
    while True:
        if visited[cur] != 0:
            visited[cur] -= 1
            dummy[cur//sqrtN] -= 1
            print(cur)
            break
        cur += 1