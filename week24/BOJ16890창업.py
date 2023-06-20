from collections import deque

gu = input()
cube = input()
gu = sorted(gu)
cube = sorted(cube,reverse=True)
n = len(gu)

gu = deque(gu[:n-n//2])
cube = deque(cube[:n//2])

ans = ['']*n
idx,rIdx = 0,n-1
flag = True
for i in range(n):
    cur = gu if flag else cube

    if gu and cube and gu[0] >= cube[0]:
        ans[rIdx] = cur.pop()
        rIdx -= 1
    else:
        ans[idx] = cur.popleft()
        idx += 1
    flag = not flag

print(''.join(ans))