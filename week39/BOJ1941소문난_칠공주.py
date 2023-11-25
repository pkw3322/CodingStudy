import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def outOfRange(x,y):
    return x < 0 or x >= 5 or y < 0 or y >= 5;

def check(num):
    global available
    x = num // 5
    y = num % 5
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if outOfRange(nx,ny) or visited[nx][ny]:
            continue
        nextNum = nx*5 + ny
        if nextNum in p:
            visited[nx][ny] = 1
            available += 1
            check(nextNum)
def dfs(depth,cntY, index):
    global result, available, visited
    if cntY > 3 or 25-index < 7-depth:
        return

    if depth == 7:                  
        available = 1              
        visited = [[0] * 5 for _ in range(5)]
        sr, sc = p[0]//5, p[0]%5    
        visited[sr][sc] = 1       
        check(p[0])     
        if available == 7:       
            result += 1
        return

    r = index // 5    
    c = index % 5

    if A[r][c] == "Y":             
        p.append(index)
        dfs(depth+1, cntY+1, index+1)
        p.pop()
    else:                  
        p.append(index)
        dfs(depth+1, cntY, index+1)
        p.pop()
    dfs(depth, cntY, index+1)

A = [input().rstrip() for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
result = 0
p = []
dfs(0, 0, 0)
print(result)
