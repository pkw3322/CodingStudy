import sys

input = sys.stdin.readline

n = int(input())
alphas = [[0]*58 for _ in range(58)]
cnt = 0

for _ in range(n):
    str = input()
    if str[0] == str[5]:
        continue
    if not alphas[ord(str[0]) - 65][ord(str[5]) - 65]:
        alphas[ord(str[0]) - 65][ord(str[5]) - 65] = 1
        cnt += 1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i != j and (not alphas[i][j]) and alphas[i][k] and alphas[k][j]:
                alphas[i][j] = 1
                cnt += 1

print(cnt)

for i in range(58):
    for j in range(58):
        if alphas[i][j]:
            print(chr(i+65),"=>",chr(j+65))