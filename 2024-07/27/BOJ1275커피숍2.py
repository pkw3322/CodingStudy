import sys
from math import ceil,log2
input = sys.stdin.readline

def initTree(start, end, idx):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = initTree(start,mid,idx*2) + initTree(mid+1,end,idx*2+1)
    return tree[idx]

def findSum(start,end, left, right, idx):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start+end)//2
    return findSum(start,mid,left,right,idx*2) + findSum(mid+1,end,left,right,idx*2+1)

def updateTree(start, end, idx, target, value):
    if start > target or end < target:
        return
    if start == end:
        tree[idx] = value
        return
    mid = (start+end)//2
    updateTree(start,mid,idx*2,target,value)
    updateTree(mid+1,end,idx*2+1,target,value)
    tree[idx] = tree[idx*2] + tree[idx*2+1]

n, q = map(int, input().split())
nums = list(map(int, input().split()))
tree = [0]*(1<<(int(ceil(log2(n))+1)))

initTree(0,n-1,1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x,y = y,x
    print(findSum(0,n-1,x-1,y-1,1))
    updateTree(0,n-1,1,a-1,b)
    