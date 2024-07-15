import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

index = [0]*(n+1)

def getPreOrder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return
    root = postOrder[postEnd]
    print(root, end=" ")

    left = index[root] - inStart
    right = inEnd - index[root]

    getPreOrder(inStart, inStart + left - 1, postStart, postStart + left - 1)
    getPreOrder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)

for i in range(n):
    index[inOrder[i]] = i

getPreOrder(0,n-1,0,n-1)
print()