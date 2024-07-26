import sys

input = sys.stdin.readline

x, y, w, s = map(int, input().split())

ans = 0
if 2*w <= s:
    ans = x*w + y*w
else:
    small = min(x,y)
    big = max(x,y)
    diff = big - small
    ans = small * s
    if w <= s:
        ans += diff * w
    else:
        if diff % 2 == 0:
            ans += diff * s
        else:
            ans += (diff-1) * s + w

print(ans)