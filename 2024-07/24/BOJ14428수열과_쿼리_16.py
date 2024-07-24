import sys
from math import log2, ceil

input = sys.stdin.readline

def initTree(start, end, idx):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = min(initTree(start,mid, idx*2), initTree(mid+1,end, idx*2+1))
    return tree[idx]

def findMin(start, end, idx, left, right):
    if left > end or right < start:
        return [int(1e9),int(1e9)]
    if left <= start and end <= right:
        return tree[idx]
    mid = (start+end)//2
    return min(findMin(start,mid,idx*2,left,right), findMin(mid+1,end,idx*2+1,left,right))

def updateTree(start, end, idx, target, value):
    if start > target or end < target:
        return
    if start == end:
        tree[idx] = value
        return
    mid = (start+end)//2
    updateTree(start,mid,idx*2,target,value)
    updateTree(mid+1,end,idx*2+1,target,value)
    tree[idx] = min(tree[idx*2], tree[idx*2+1])

n = int(input())
temp = list(map(int,input().split()))
nums = []
for i in range(n):
    nums.append([temp[i],i+1])
    
m = int(input())
tree = [0] * (1 << int(ceil(log2(n)) + 1))

initTree(0,n-1,1)

for _ in range(m):
    a,b,c = map(int,input().split())
    if a == 1:
        nums[b-1][0] = c
        updateTree(0,n-1,1,b-1,nums[b-1])
    else:
        print(findMin(0,n-1,1,b-1,c-1)[1])

