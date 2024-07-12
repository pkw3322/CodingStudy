import sys

input = sys.stdin.readline

t = int(input())

counts = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
maxDP = [""] * 101
minDP = [sys.maxsize] * 101

minDP[2] = 1
minDP[3] = 7
minDP[4] = 4
minDP[5] = 2
minDP[6] = 6
minDP[7] = 8

def calculateMax(n):
    if maxDP[n] != "":
        return maxDP[n]
    
    if n == 0:
        return ""
    
    if n % 2 == 0:
        maxDP[n] = "1" + calculateMax(n-2)
    else:
        maxDP[n] = "7" + calculateMax(n-3)

    return maxDP[n]

def calculateMin(n):
    if minDP[n] != sys.maxsize:
        return str(minDP[n])

    for i in range(2, n-1):
        minDP[n] = min(minDP[n], int(calculateMin(i) + calculateMin(n-i)))
        if i == 6:
            minDP[n] = min(minDP[n], int(calculateMin(n-6) + "0"))

    return str(minDP[n])

for _ in range(t):
    n = int(input())

    maxNum = calculateMax(n)
    minNum = calculateMin(n)

    print(minNum + " " + maxNum)

