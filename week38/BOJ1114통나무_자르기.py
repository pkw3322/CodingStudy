import sys

input = sys.stdin.readline

l,k,c = map(int,input().split())

positions = [0] + sorted(list(map(int, input().split()))) + [l]
diffs = [positions[idx+1] - positions[idx] for idx in range(k + 1)]
maxDiff = max(diffs)

left,right = 0,l

def getCount(mid):
    if maxDiff > mid:
        return 10001,0
    s, cnt = 0, 0
    for p in diffs[::-1]:
        s += p
        if s > mid:
            s = p
            cnt += 1
    return cnt, s if cnt == c else diffs[0]


while left <= right:
    mid = (left + right) // 2
    cnt,start = getCount(mid)

    if cnt <= c:
        ans_max = mid
        ans_start = start
        right = mid - 1
    else:
        left = mid + 1

print(ans_max,ans_start)