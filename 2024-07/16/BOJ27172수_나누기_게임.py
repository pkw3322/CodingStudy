import sys

input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))
maxCard = max(cards)
cardsIdx = {}
for i in range(n):
    cardsIdx[cards[i]] = i

dp = [0]*n

for i in range(n):
    cur = cards[i]
    for j in range(cur*2, maxCard+1, cur):
        if j in cardsIdx:
            idx = cardsIdx[j]
            dp[idx] -= 1
            dp[i] += 1

print(*dp)