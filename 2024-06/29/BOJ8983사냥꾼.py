import sys

input = sys.stdin.readline

m, n, l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()
animals = [list(map(int, input().split())) for _ in range(n)]

answer = 0
idx = 0

for x,y in animals:
    s,e = 0, m-1
    mid = 0
    while s <= e:
        mid = (s+e)//2
        if shoot[mid] < x:
            s = mid + 1
        else:
            e = mid - 1
    if abs(shoot[mid]-x) + y <= l:
        answer += 1
    elif mid < m-1 and abs(shoot[mid+1]-x) + y <= l:
        answer += 1
    elif mid > 0 and abs(shoot[mid-1]-x) + y <= l:
        answer += 1

print(answer)