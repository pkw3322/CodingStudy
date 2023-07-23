import sys
input=sys.stdin.readline

r,c = map(int,input().split())
arr = []
check = [[] for i in range(c)]
for _ in range(r):
    arr.append(list(input().rstrip()))
n = int(input())

def falling(x, y, line):
    while True:
        check[line].append([x, y])
        if x+1 == r or arr[x+1][y] == "X":
            arr[x][y] = "O"
            return
        if arr[x+1][y] == "O":
            if y-1 >= 0 and arr[x][y-1] == "." and arr[x+1][y-1] == ".":
                y -= 1
            elif y+1 < c and arr[x][y+1] == "." and arr[x+1][y+1] == ".":
                y += 1
            else:
                arr[x][y] = "O"
                return
        x += 1

for _ in range(n):
    line = int(input())-1
    
    while check[line]:
        cx, cy = check[line][-1]
        if arr[cx][cy] == '.':
            break
        check[line].pop()
 
    if check[line]:
        cx, cy = check[line].pop()
        falling(cx, cy, line)
    else:
        falling(0, line, line)
 
    cx, cy = check[line].pop()
    arr[cx][cy] = "O"
 
for a in arr:
    print("".join(a))
