import sys

input = sys.stdin.readline

n,l = map(int,input().split())
floors = []

for _ in range(n):
    x,y = map(int,input().split())
    if y == 0:
        floors.append([0,x,y])
    else:
        floors.append([l-x,l,y])

def goUp(cur) :
    curUp = cur + 1
    curLeft,curRight = floors[cur][0], floors[cur][1]
    curUpLeft,curUpRight = floors[curUp][0],floors[curUp][1]
    if curUpLeft <= curLeft and curRight <= curUpRight:
        return curUp
    if curLeft <= curUpLeft and curUpRight <= curRight:
        return curUp
    if curUpLeft <= curLeft <= curUpRight:
        return curUp
    if curUpLeft <= curRight <= curUpRight:
        return curUp
    return cur

def move(cur):
    for idx in range(cur,n):
        _,_,y = floors[idx]
        if y == 0:
            floors[idx][0] += 1
            floors[idx][1] += 1
            if floors[idx][1] == l:
                floors[idx][2] = 1
        else:
            floors[idx][0] -= 1
            floors[idx][1] -= 1
            if floors[idx][0] == 0:
                y = 0

res = 0
cur = 0
toGo = n-1

while True:
    if cur == toGo:
        break
    next = goUp(cur)
    if cur == next:
        move(cur)
        res += 1
    else:
        cur = next

print(res)