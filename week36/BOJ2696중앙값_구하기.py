import sys
from heapq import heappush,heappop

input = sys.stdin.readline

def getMiddles():
    Min,Max,ans = [],[],[arr[0]]
    middle = arr[0]

    for i in range(1,len(arr)):
        num = arr[i]
        if num < middle:
            heappush(Min, -num)
        else:
            heappush(Max, num)
        
        if i % 2 == 0:
            if len(Min) < len(Max):
                heappush(Min, -middle)
                middle = heappop(Max)
            elif len(Min) > len(Max):
                heappush(Max, middle)
                middle = -heappop(Min)
            ans.append(middle)
    print(n//2+1)
    for i in range(len(ans)):
        if i != 0 and i % 10 == 0:
            print()
        print(ans[i], end=' ')
    print()

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    arr = []
    for _ in range(n//10+1):
        arr += list(map(int,input().split()))
    getMiddles()