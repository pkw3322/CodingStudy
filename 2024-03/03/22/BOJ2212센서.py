import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
weights = list(map(int,input().split()))

weights.sort()

diff = []

for i in range(n-1):
    diff.append(weights[i+1] - weights[i])

diff.sort()

print(sum(diff[:n-k]))