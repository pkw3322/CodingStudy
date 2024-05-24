import sys
from itertools import permutations

input = sys.stdin.readline

test = int(input())

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

isPrimeSet = {}

for _ in range(test):
    n = input().rstrip()

    arr = [int(i) for i in n]

    res = 0
    visited = {}
    for i in range(1,len(arr)+1):
        
        for temp in permutations(arr,i):
            num = 0
            for k in range(len(temp)):
                num += temp[k]*(10**k)
            if num not in visited:
                if num in isPrimeSet:
                    res += 1
                    visited[num] = 1
                else:
                    if isPrime(num):
                        res += 1
                        visited[num] = 1
                        isPrimeSet[num] = 1
                visited[num] = 1

    print(res)
    