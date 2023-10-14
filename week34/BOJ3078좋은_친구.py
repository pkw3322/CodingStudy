from collections import deque

n,k = map(int,input().split())
nameList = [len(input()) for _ in range(n)]
goodCount = 0

rankList = [deque() for _ in range(21)]

for i in range(len(nameList)):
    val = nameList[i]
    while rankList[val] and rankList[val][0] < i - k:
        rankList[val].popleft()
    
    if rankList[val]:
        goodCount += len(rankList[val])
    
    rankList[val].append(i)

print(goodCount)
