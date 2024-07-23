import sys

input = sys.stdin.readline

while True:
    n, *heights = list(map(int,input().split()))
    if n == 0:
        break
    stack = []
    answer = 0
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            answer = max(answer, h*w)
        stack.append(i)
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        answer = max(answer, h*w)
    print(answer)