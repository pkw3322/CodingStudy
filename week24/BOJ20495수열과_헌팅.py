import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

n = int(input())
maxs = []
mins = []
first = []
second = []

for i in range(n):
    num,error = map(int,input().split())
    first.append(num-error)
    second.append(num+error)
    maxs.append(num+error)
    mins.append(num-error)
maxs.sort()
mins.sort()

for i in range(n):
    a = bisect_left(maxs,first[i]) + 1
    b = bisect_right(mins,second[i])
    print(a,b)

