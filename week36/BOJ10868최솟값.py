import sys
import math
input = sys.stdin.readline

def buildTree(index,left,right):
    if left == right:
        segTree[index] = nums[left]
        return segTree[index]
    mid = (left+right)//2

    leftTree = buildTree(index*2,left,mid)
    rightTree = buildTree(index*2+1,mid+1,right)
    segTree[index] = min(leftTree,rightTree)
    return segTree[index]

def findValue(index,left,right):
    if end < left or start > right:
        return sys.maxsize
    if left >= start and right <= end:
        return segTree[index]
    
    mid = (left+right)//2
    leftValue = findValue(index*2,left,mid)
    rightValue = findValue(index*2+1,mid+1,right)
    return min(leftValue,rightValue)

n,m = map(int,input().split())
nums = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))+1
nodeNum = 1 << h
segTree = [0 for _ in range(nodeNum)]
buildTree(1,0,n-1)

for _ in range(m):
    start,end = map(int,input().split())
    start -= 1
    end -= 1
    print(findValue(1,0,n-1))