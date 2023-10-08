import sys
from collections import deque

input = sys.stdin.readline

def turn(a):
    global direct
    if a == 'L':
        direct = (direct-1)%4
    elif a == 'D':
        direct = (direct+1)%4

def bfs():
    global direct
    cnt = 0
    x,y = 0,0
    while True:
        cnt += 1
        x += dx[direct]
        y += dy[direct]
        if x < 0 or x >= n or y < 0 or y >= n:
            break

        if board[x][y] == 2:
            board[x][y] = 1
            q.append((x,y))
            if cnt in directionDict:
                turn(directionDict[cnt])
        
        elif board[x][y] == 0:
            board[x][y] = 1
            q.append((x,y))
            tailx,taily = q.popleft()
            board[tailx][taily] = 0
            if cnt in directionDict:
                turn(directionDict[cnt])
        else:
            break
    return cnt

n = int(input())
k = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

board = [[0 for _ in range(n)] for _ in range(n)]
apples = []
for _ in range(k):
    x,y = map(int,input().split())
    apples.append((x,y))
    board[x-1][y-1] = 2

l = int(input())
directionDict = dict()
q = deque()
q.append((0,0))
for _ in range(l):
    x,c = input().split()
    directionDict[int(x)] = c

board[0][0] = 1
direct = 0
print(bfs())
