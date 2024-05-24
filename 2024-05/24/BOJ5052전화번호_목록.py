import sys

input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    strList = [input().rstrip() for _ in range(n)]
    strList.sort()
    flag = False
    for i in range(n-1):
        length = len(strList[i])
        if strList[i] == strList[i+1][:length]:
            print('NO')
            flag = True
            break
    if not flag:
        print('YES')
