import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n,m = map(int,input().split())
    students = [list(map(int,input().split())) for _ in range(m)]
    students.sort(key=lambda x: x[1])
    books = [0]*(n+1)
    ans = 0
    for s,e in students:
        for i in range(s,e+1):
            if books[i] == 0:
                books[i] = 1
                ans += 1
                break
    print(ans)
    