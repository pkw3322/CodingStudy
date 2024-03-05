import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    M,N,x,y = map(int,input().split())
    k = x
    flag = True
    while k <= M*N:
        if (k-x)%M == 0 and (k-y)%N == 0:
            print(k)
            flag = False
            break
        k += M
    if flag:
        print(-1)