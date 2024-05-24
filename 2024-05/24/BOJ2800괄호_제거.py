import sys

input = sys.stdin.readline

string = input().rstrip()
stack = []
pairIdx = []
res = []

for idx, c in enumerate(string):
    if c == '(':
        stack.append(idx)
    elif c == ')':
        pairIdx.append([stack.pop(),idx])
n = len(pairIdx)

for i in range(1<<n):
    temp = list(string)
    for j in range(n):
        if i & 1<<j:
            temp[pairIdx[j][0]] = ''
            temp[pairIdx[j][1]] = ''
    res.append(''.join(temp))
res = list(filter(lambda x: x != '' and x != string,res))
print('\n'.join(sorted(set(res))))