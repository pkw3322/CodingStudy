import sys

input = sys.stdin.readline

n = int(input())

words = {}
for _ in range(n):
    word = input().split()[1:]
    cur = words
    for w in word:
        if w not in cur:
            cur[w] = {}
        cur = cur[w]

def dfs(cur, depth):
    for key in sorted(cur):
        print("--"*depth + key)
        dfs(cur[key], depth+1)
for i in sorted(words):
    print(i)
    dfs(words[i], 1)
    