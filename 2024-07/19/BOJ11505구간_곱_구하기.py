import sys
from math import log2, ceil
input = sys.stdin.readline

def initTree(start,end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = (initTree(start,mid, idx*2) * initTree(mid+1,end, idx*2+1)) % toMod
    return tree[idx]

def findMul(start, end, idx, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[idx]
    mid = (start+end)//2
    return (findMul(start,mid,idx*2,left,right) * findMul(mid+1,end,idx*2+1,left,right)) % toMod

def updateTree(start, end, idx, target, value):
    if start > target or end < target:
        return
    if start == end:
        tree[idx] = value
        return
    mid = (start+end)//2
    updateTree(start,mid,idx*2,target,value)
    updateTree(mid+1,end,idx*2+1,target,value)
    tree[idx] = (tree[idx*2] * tree[idx*2+1]) % toMod

toMod = 1000000007
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0] * (1 << int(ceil(log2(n)) + 1))

initTree(0, n-1, 1)

for _ in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        updateTree(0,n-1,1,b-1,c)
    else:
        print(findMul(0,n-1,1,b-1,c-1))
