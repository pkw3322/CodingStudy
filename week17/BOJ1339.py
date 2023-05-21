import sys

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]

alpha_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alpha_list = []
ans = 0

for alpha in arr:
    for i in range(len(alpha)):
        num = 10**(len(alpha)-i-1)
        alpha_dict[alpha[i]] += num

for val in alpha_dict.values():
    if val > 0:
        alpha_list.append(val)

alpha_list = sorted(alpha_list,reverse=True)
for i in range(len(alpha_list)):
    ans += alpha_list[i]*(9-i)

print(ans)