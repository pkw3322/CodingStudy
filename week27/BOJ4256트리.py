import sys

input = sys.stdin.readline

def getPostOrder(preOrder,inOrder):
    if len(preOrder) == 0:
        return
    elif len(preOrder) == 1:
        print(preOrder[0],end=' ')
        return
    elif len(preOrder) == 2:
        print(preOrder[1],preOrder[0],end=' ')
        return
    
    root = inOrder.index(preOrder[0])

    leftIn = inOrder[0:root]
    leftPre = preOrder[1:1+len(leftIn)]
    getPostOrder(leftPre,leftIn)

    rightIn = inOrder[root+1:]
    rightPre = preOrder[len(leftPre)+1:]
    getPostOrder(rightPre,rightIn)

    print(preOrder[0],end=' ')

t = int(input())

for _ in range(t):
    n = int(input())
    preOrder = list(map(int,input().split()))
    inOrder = list(map(int,input().split()))

    getPostOrder(preOrder,inOrder)
    print()