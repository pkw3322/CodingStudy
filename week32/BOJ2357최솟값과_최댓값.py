import sys
import math

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def buildSegTree(index, left, right):
    if left == right:
        segTree[index] = (nums[left],nums[left])
        return segTree[index]
    mid = (left+right)//2

    leftTree = buildSegTree(index*2,left,mid)
    rightTree = buildSegTree(index*2+1,mid+1,right)

    segTree[index] = [min(leftTree[0],rightTree[0]),max(leftTree[1],rightTree[1])]

    return segTree[index]

def findValue(index, left, right):
    if end < left or start > right:
        return [sys.maxsize, 0]
    if left >= start and end >= right:
        return segTree[index]
    
    mid = (left+right)//2
    leftAns = findValue(index*2,left,mid)
    rightAns = findValue(index*2+1,mid+1,right)
    return [min(leftAns[0],rightAns[0]),max(leftAns[1],rightAns[1])]

n,m = map(int,input().split())
nums = [int(input()) for _ in range(n)]
height = math.ceil(math.log2(n)) + 1
nodeNum = 1 << height
segTree = [[0,0] for _ in range(nodeNum)]

buildSegTree(1,0,n-1)

for i in range(m):
    start,end = map(int,input().split())
    start -= 1
    end -= 1
    ans = findValue(1, 0, n-1)
    print(ans[0], ans[1])