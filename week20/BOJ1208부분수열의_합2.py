import sys
from itertools import combinations
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
def countNum(arr, target):
    return bisect_right(arr,target) - bisect_left(arr,target)

def getSumArr(arr):
    res = []
    for i in range(1,len(arr)+1):
        com = combinations(arr,i)
        for tem in com:
            res.append(sum(tem))
    res.sort()
    return res

def func():
    global cnt
    mid = n//2
    leftArr = arr[:mid]
    rightArr = arr[mid:]
    left = getSumArr(leftArr)
    right = getSumArr(rightArr)
    for l in left:
        target = s - l
        cnt += countNum(right,target)
    cnt += countNum(left,s)
    cnt += countNum(right,s)

func()
print(cnt)