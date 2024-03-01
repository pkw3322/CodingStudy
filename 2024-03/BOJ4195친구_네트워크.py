import sys

input = sys.stdin.readline

testCase = int(input())

def find(x):
    parentX = parent[x]
    
    if parentX == x:
        return x
    else:
        parent[x] = find(parentX)
        return parent[x]
    
def union(x,y):
    x = find(x)
    y = find(y)
    if parent[x] != parent[y]:
        parent[y] = x
        dic[x] += dic[y]
    print(dic[x])
    
for _ in range(testCase):
    n = int(input())
    parent = {}
    dic = {}
    for _ in range(n):
        a,b = input().split()
        if a not in parent:
            parent[a] = a
            dic[a] = 1
        if b not in parent:
            parent[b] = b
            dic[b] = 1
        union(a,b)
         
