import sys

n,m = map(int,sys.stdin.readline().split())
knowList = set(sys.stdin.readline().split()[1:])
parties = []
for _ in range(m):
    parties.append(set(sys.stdin.readline().split()[1:]))

for _ in range(m):
    for party in parties:
        if party&knowList:
            knowList = knowList.union(party)

ans = 0

for party in parties:
    if party & knowList : 
        continue
    ans += 1

print(ans)