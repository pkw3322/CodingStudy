import sys
import math

input = sys.stdin.readline

a,b = map(int, input().split())
ans = 0
def calc(n):
    if n <= 0:
        return 0
    lg2 = int(math.log2(n))
    if n == 2**lg2:
        return lg2*n//2 + 1
    dif = n - 2**lg2
    return calc(2**lg2) + dif + calc(dif)

ans = calc(b) - calc(a-1)

print(ans)

# 2 = 0010
# 3 = 0011
# 4 = 0100
# 5 = 0101
# 6 = 0110
# 7 = 0111
# 8 = 1000
# 9 = 1001
# 10 = 1010
# 11 = 1011
# 12 = 1100