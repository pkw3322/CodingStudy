import sys
from heapq import heappop, heappush

input = sys.stdin.readline

k, n = map(int, input().split())
primes = list(map(int, input().split()))

heap = []
for i in range(k):
    heappush(heap, (primes[i], i))

for i in range(n):
    num, idx = heappop(heap)
    if i == n-1:
        print(num)
        break
    for i in range(k):
        heappush(heap, (primes[i]*num, i))
        if num % primes[i] == 0:
            break

