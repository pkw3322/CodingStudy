import sys

n,m = map(int,sys.stdin.readline().split())

def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)

print(m - gcd(n,m))