import sys

input = sys.stdin.readline

t = input().rstrip()
p = input().rstrip()

n = len(t)
m = len(p)

# pattern string p의 prefix와 suffix가 같은 최대 길이를 저장
pi = [0]*m
j = 0
for i in range(1,m):
    while j > 0 and p[i] != p[j]:
        j = pi[j-1]

    if p[i] == p[j]:
        j += 1
        pi[i] = j


# KMP 알고리즘
res = []
j = 0
for i in range(n):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]
    
    if t[i] == p[j]:
        if j == m-1:
            res.append(i-m+2)
            j = pi[j]
        else:
            j += 1

print(len(res))
print(*res)