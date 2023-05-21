import sys
import math
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    points = []
    totalX,totalY = 0,0
    for _ in range(n):
        x,y = map(int,input().split())
        totalX += x
        totalY += y
        points.append((x,y))
    ans = sys.maxsize
    com = combinations(range(n),n//2)
    for c in com:
        sumX,sumY = totalX,totalY

        for i in c:
            sumX -= 2*points[i][0]
            sumY -= 2*points[i][1]
        
        scala = math.sqrt(sumX**2 + sumY**2)
        if ans > scala:
            ans = scala
    print(ans)