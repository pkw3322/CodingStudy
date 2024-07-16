import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
start = "".join(map(str, arr))

m = int(input())
graphs = [tuple(map(int, input().split())) for _ in range(m)]

ans = 0

q = []
heappush(q,(0,arr))
dic = {}
dic[start] = 0

def shuffle(base, l, r):
    res = []
    res.extend(base[:l-1])
    res.append(base[r-1])
    res.extend(base[l:r-1])
    res.append(base[l-1])
    res.extend(base[r:])
    return res

while q:
    cost, now = heappop(q)
    stringNow = ''.join(map(str,now))
    if stringNow in dic and dic[stringNow] < cost:
        continue
    for nl,nr,nc in graphs:
        nextShuffle = shuffle(now,nl,nr)
        stringNext = ''.join(map(str,nextShuffle))
        nextCost = cost + nc
        if stringNext not in dic or dic[stringNext] > nextCost:
            dic[stringNext] = nextCost
            heappush(q,(nextCost,nextShuffle))

ans = ''.join(map(str,sorted(arr)))

print(dic[ans] if ans in dic else -1)
