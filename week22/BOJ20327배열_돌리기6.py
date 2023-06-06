import sys

input = sys.stdin.readline

n,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2**n)]
def act1(b):
    sqrB = 2**b
    for k in range(2**(n-b)):
            for l in range(2**(n-b)):
                next = [[0]*sqrB]*sqrB
                tk = sqrB*k
                tl = sqrB*l
                for i in range(sqrB):
                    next[i] = arr[tk+i][tl:tl+sqrB]
                for i in range(sqrB):
                    for j in range(sqrB):
                        arr[tk+i][tl+j] = next[sqrB-i-1][j]
def act2(b):
    sqrB = 2**b
    for k in range(2**(n-b)):
            for l in range(2**(n-b)):
                next = [[0]*sqrB]*sqrB
                tk = sqrB*k
                tl = sqrB*l
                for i in range(sqrB):
                    next[i] = arr[tk+i][tl:tl+sqrB]
                for i in range(sqrB):
                    for j in range(sqrB):
                        arr[tk+i][tl+j] = next[i][sqrB-j-1]
def act3(b):
    sqrB = 2**b
    for k in range(2**(n-b)):
            for l in range(2**(n-b)):
                temp = [[0]*sqrB]*sqrB
                tk = sqrB*k
                tl = sqrB*l
                for i in range(sqrB):
                    temp[i] = arr[tk+i][tl:tl+sqrB]

                next = [[0]*sqrB for _ in range(sqrB)]
                for i in range(sqrB):
                    for j in range(sqrB):
                        next[i][j] = temp[sqrB-j-1][i]
                for i in range(sqrB):
                    for j in range(sqrB):
                        arr[tk+i][tl+j] = next[i][j]
def act4(b):
    sqrB = 2**b
    for k in range(2**(n-b)):
            for l in range(2**(n-b)):
                temp = [[0]*sqrB]*sqrB
                tk = sqrB*k
                tl = sqrB*l
                for i in range(sqrB):
                    temp[i] = arr[tk+i][tl:tl+sqrB]  

                next = [[0]*sqrB for _ in range(sqrB)]
                for i in range(sqrB):
                    for j in range(sqrB):
                        next[i][j] = temp[j][sqrB-i-1]
                for i in range(sqrB):
                    for j in range(sqrB):
                        arr[tk+i][tl+j] = next[i][j]
for i in range(r):
    a,b = map(int,input().split())
    if a == 1:
        act1(b)
    elif a == 2:
        act2(b)
    elif a == 3:
        act3(b)             
    elif a == 4:
        act4(b)
    elif a == 5:
        act1(b)
        act1(n)
    elif a == 6:
        act2(b)
        act2(n)
    elif a == 7:
        act3(n)
        act4(b)
    elif a == 8:
        act4(n)
        act3(b)
for a in arr:
    print(" ".join(map(str,a)))