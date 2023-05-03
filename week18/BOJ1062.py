import sys

n, k = map(int, input().split())
answer = 0

haveToKnow = {'a','n','t','i','c'}
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

if k < 5 : 
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

learned = [0] * 26
for x in haveToKnow:
    learned[ord(x) - ord('a')] = 1
def dfs(count,index):
    global answer
    
    if count == k-5:
        canRead = 0
        for word in words:
            checker = True
            for w in word:
                if not learned[ord(w) - ord('a')]:
                    checker = False
                    break
            if checker:
                canRead += 1
        answer = max(answer,canRead)
        return
    for i in range(index,26):
        if not learned[i]:
            learned[i] = True
            dfs(count+1,i)
            learned[i] = False
dfs(0,0)
print(answer)