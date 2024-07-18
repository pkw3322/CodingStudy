import sys

input = sys.stdin.readline

toMod = 1000000007

n = int(input())
foods = list(map(int, input().split()))
foods.sort()

def pow(a,b):
    if b == 0:
        return 1
    half = pow(a,b//2)
    if b % 2:
        return (half*half*a) % toMod
    return (half*half) % toMod
ans = 0
for i in range(n):
    ans += foods[i] * pow(2,i)
    ans -= foods[i] * pow(2,n-i-1)
    ans %= toMod

print(ans)