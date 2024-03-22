n = int(input())

res = []

def check(result,cnt):
    for i in range(1,(cnt//2) + 1):
        if result[-i:] == result[-2*i:-i]:
            return False
    return True

def BackTracking(cnt):
    if not check(res,cnt):
        return -1
    if cnt == n:
        print(*res,sep='')
        return 1
    for i in range(1,4):
        res.append(i)
        if BackTracking(cnt+1) == 1:
            return 1
        res.pop()

BackTracking(0)
