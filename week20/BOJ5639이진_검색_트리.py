import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = []
while True:
    try:
        num = int(input())
        tree.append(num)
    except:
        break

def binarySearchTree(left,right):
    if left > right:
        return
    mid = right + 1
    for i in range(left+1,right+1):
        if tree[i] > tree[left]:
            mid = i
            break
    binarySearchTree(left+1,mid-1)
    binarySearchTree(mid,right)
    print(tree[left])

binarySearchTree(0,len(tree)-1)