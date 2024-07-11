import sys

input = sys.stdin.readline

n,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def mul(matrix, mat2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix[i][k] * mat2[k][j]
            res[i][j] %= 1000
    return res

def powerMatrix(matrix, b):
    if b == 1:
        return matrix
    elif b % 2 == 1:
        temp = powerMatrix(matrix, b//2)
        mulTemp = mul(temp, temp)
        return mul(mulTemp, matrix)
    else:
        temp = powerMatrix(matrix, b//2)
        return mul(temp, temp)

ans = powerMatrix(arr, b)

for i in range(n):
    for j in range(n):
        print(ans[i][j]%1000, end = ' ')
    print()
