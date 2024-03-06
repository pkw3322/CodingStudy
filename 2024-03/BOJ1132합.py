n = int(input())
alpha = [[0,False] for _ in range(10)]
ans = 0

for _ in range(n):
    cur = input()
    cnt = 1
    alpha[ord(cur[0]) - 65][1] = True
    for i in range(len(cur)-1,-1,-1):
        alpha[ord(cur[i]) - 65][0] += cnt
        cnt *= 10

alpha.sort(reverse=True)

if alpha[-1][1]:
    for i in range(8,-1,-1):
        if not alpha[i][1]:
            del alpha[i]
            break
        
for i in range(9):
    ans += alpha[i][0]*(9-i)
print(ans)