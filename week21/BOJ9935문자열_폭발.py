import sys

str1 = sys.stdin.readline().rstrip()

bomb = sys.stdin.readline().rstrip()

ans = []
lBomb = len(bomb)

for i in range(len(str1)):
    ans.append(str1[i])
    temp = ''.join(ans[-lBomb:])
    if temp == bomb:
        for _ in range(lBomb):
            ans.pop()

if ans:
    print(''.join(ans))
else:
    print('FRULA')