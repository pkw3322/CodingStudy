from collections import deque

import sys

input = sys.stdin.readline

testCase = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def bfs():
    q = deque()
    q.append(n)
    while q:
        cur = q.popleft()
        if cur == m:
            return visited[cur]
        for digit in range(4):
            for num in range(10):
                next = list(str(cur))
                next[digit] = str(num)
                next = int(''.join(next))
                if 1000 <= next < 10000:
                    if not visited[next] and primes[next]:
                        visited[next] = visited[cur] + 1
                        q.append(next)
    return "Impossible"
primes = [False]
for i in range(1,10000):
    primes.append(isPrime(i))

for _ in range(testCase):
    n,m = map(int,input().split())
    visited = [0 for _ in range(10000)]
    visited[n] = 1
    ans = bfs()
    if ans == "Impossible":
        print(ans)
    else:
        print(ans-1)
