n,m = map(int,input().split())

ans = 0
ni = 9
digit = 1

while m > digit * ni:
    ans += ni
    m -= digit * ni
    digit += 1
    ni *= 10
res = ans + ((m-1) // digit) + 1
if res > n:
    print(-1)
else:
    print(str(res)[(m-1)%digit])