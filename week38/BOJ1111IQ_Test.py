import sys

input = sys.stdin.readline

n = int(input())
datas = list(map(int,input().split()))

if n == 1:
    print('A')
elif n == 2:
    if datas[0] == datas[1] :
        print(datas[0])
    else:
        print('A')
else:
    if datas[0] == datas[1]:
        a = 0
        b = datas[0]
    else:
        a = (datas[2] - datas[1]) // (datas[1] - datas[0])
        b = datas[1] - datas[0]*a
    
    isMatchPattern = True
    for i in range(1,n):
        if datas[i] != datas[i-1]*a + b:
            isMatchPattern = False
            break
    if not isMatchPattern:
        print('B')
    else:
        print(datas[-1]*a + b)
