import math

n = int(input())
if n == 1:
    print(2)
    exit()

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if n == 1000000:
    print(1003001)
    exit()

while True:
    if isPrime(n) and str(n) == str(n)[::-1]:
        print(n)
        break
    n += 1 