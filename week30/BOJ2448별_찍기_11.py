import sys
sys.setrecursionlimit(10**6)

star = [
    [" "," ","*"," "," "],
    [" ","*"," ","*"," "],
    ["*","*","*","*","*"]
]
n = int(input())

def recursion(cn,prev):
    after = [[" "]*(2*2*cn-1) for _ in range(2*cn)]
    for i in range(cn):
        after[i][cn:cn+2*cn-1] = prev[i]
    tem = 0
    for i in range(cn,2*cn):
        after[i][:2*cn] = prev[tem]
        after[i][2*cn:2*cn+len(prev[tem])] = prev[tem]
        tem += 1
    if 2*cn == n:
        return after
    return recursion(2*cn,after)
if n == 3:
    res = star
else:
    res = recursion(3,star)

for i in res:
    print("".join(i))