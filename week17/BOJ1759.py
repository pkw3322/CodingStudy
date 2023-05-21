import sys

def fun(count,index):
    if count == L:
        mo,za = 0,0
        for i in range(L):
            if ans[i] in mos:
                mo += 1
            else:
                za += 1
        if mo >= 1 and za >= 2 :
            print("".join(ans))
        return
    for i in range(index,C):
        ans.append(alphas[i])
        fun(count+1,i+1)
        ans.pop()

L,C = map(int,sys.stdin.readline().split())
mos = ['a','e','i','o','u']
alphas = sorted(list(map(str,sys.stdin.readline().split())))
ans = []

fun(0,0)