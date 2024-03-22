import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

stack = []
ans = []

for i in range(n):
    if not stack:
        ans.append(0)
        stack.append((arr[i],i+1))
    else:
        while stack and stack[-1][0] < arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1][1])
        else:
            ans.append(0)
        stack.append((arr[i],i+1))
print(*ans)
