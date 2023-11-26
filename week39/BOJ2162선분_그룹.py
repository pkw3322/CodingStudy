import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    px = find(x)
    py = find(y)
    if px > py:
        px,py = py,px
    parent[py] = px

def checkCross(line1,line2):
    p1 = (line1[0],line1[1])
    p2 = (line1[2],line1[3])
    p3 = (line2[0],line2[1])
    p4 = (line2[2],line2[3])

    if p1 > p2 :
        p1,p2 = p2,p1
    if p3 > p4:
        p3,p4 = p4,p3
    
    p12 = (p2[0]-p1[0],p2[1]-p1[1])
    p13 = (p3[0]-p1[0],p3[1]-p1[1])
    p14 = (p4[0]-p1[0],p4[1]-p1[1])

    tri1 = p12[0]*p13[1] - p12[1]*p13[0]
    tri2 = p12[0]*p14[1] - p12[1]*p14[0]

    if tri1*tri2 <= 0:
        if tri1 == 0 and tri2 == 0:
            return p1 <= p3 <= p2 or p1 <= p4 <= p2 or p3 <= p1 <= p4 or p3 <= p2 <= p4
        return True
    else:
        return False

n = int(input())
graph = [0 for _ in range(n)]
parent = [i for i in range(n)]

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    graph[i] = (x1,y1,x2,y2)

for i in range(n-1):
    for j in range(i+1,n):
        if checkCross(graph[i],graph[j]) and checkCross(graph[j],graph[i]):
            if find(i) != find(j):
                union(i,j)

for i in range(n):
    find(i)
print(len(set(parent)))

parent.sort()
cnt = 1
maxCount = 1
for i in range(1,n):
    cnt = cnt+1 if parent[i-1] == parent[i] else 1
    maxCount = max(maxCount,cnt)

print(maxCount)