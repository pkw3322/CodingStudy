import sys

input = sys.stdin.readline

n = int(input())
cnt = 0

def phi(n):
    global cnt
    if n == 1:
        return 1
    result = n
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            while n%i == 0:
                n //= i
            result *= (1-1/i)
    
    if n > 1:
        result *= (1-1/n)
    return int(result)

print(phi(n))
