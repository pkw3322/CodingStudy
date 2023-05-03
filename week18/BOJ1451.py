import sys

n,m = map(int,sys.stdin.readline().split())
	
arr = [[0 for _ in range(m + 1)]]
 
 
for _ in range(n):
    line_input = [0] + list(map(int, list(input())))
    arr.append(line_input)

ans = 0

s = [[0]*(m+1) for _ in range(n+1)]
for r in range(1,n+1):
    for c in range(1,m+1):
        s[r][c] = s[r][c-1] + s[r-1][c] - s[r-1][c-1] + arr[r][c]

def calculate(x1,y1,x2,y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]

for i in range(1,n-1):
    for j in range(i+1,n):
        r1 = calculate(1,1,i,m)
        r2 = calculate(i+1,1,j,m)
        r3 = calculate(j+1,1,n,m)
        ans = max(ans,r1*r2*r3)

for i in range(1,m-1):
    for j in range(i+1,m):
        r1 = calculate(1,1,n,i)
        r2 = calculate(1,i+1,n,j)
        r3 = calculate(1,j+1,n,m)
        ans = max(ans,r1*r2*r3)

for i in range(1,m):
    for j in range(1,n):
        r1 = calculate(1,1,n,i)
        r2 = calculate(1,i+1,j,m)
        r3 = calculate(j+1,i+1,n,m)
        ans = max(ans,r1*r2*r3)

for i in range(1,n):
    for j in range(1,m):
        r1 = calculate(1,1,i,j)
        r2 = calculate(i+1,1,n,j)
        r3 = calculate(1,j+1,n,m)
        ans = max(ans,r1*r2*r3)

for i in range(1,n):
    for j in range(1,m):
        r1 = calculate(1,1,i,m)
        r2 = calculate(i+1,1,n,j)
        r3 = calculate(i+1,j+1,n,m)
        ans = max(ans,r1*r2*r3)

for i in range(1,n):
    for j in range(1,m):
        r1 = calculate(1,1,i,j)
        r2 = calculate(1,j+1,i,m)
        r3 = calculate(i+1,1,n,m)
        ans = max(ans,r1*r2*r3)

print(ans)