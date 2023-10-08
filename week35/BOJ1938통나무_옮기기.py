import sys
input = sys.stdin.readline
from collections import deque

def checkDir(temp):
    if temp[0][1] == temp[1][1]:
        return 0
    return 1

def checkVisited(temp, d, cnt):
    if temp not in visited:
        visited.add(temp)
        q.append((temp, d, cnt+1))

def bfs():
    while q:
        newTemp, d, cnt = q.popleft()
        if newTemp == goal:
            return cnt

        if d == 0:
            for cmd in range(5):
                # U
                if cmd == 0:
                    col = deque(newTemp)
                    r, c = col[0]
                    if (0 <= r-1 < N) and plain[r-1][c] == "0":
                        col.pop()
                        col.appendleft((r-1, c))
                        checkVisited(tuple(col), 0, cnt)

                # D
                elif cmd == 1:
                    col = deque(newTemp)
                    r, c = col[-1]
                    if (0 <= r+1 < N) and plain[r+1][c] == "0":
                        col.popleft()
                        col.append((r+1, c))
                        checkVisited(tuple(col), 0, cnt)

                # L
                elif cmd == 2:
                    flag = 1
                    for r, c in newTemp:
                        if not (0 <= c-1 < N) or plain[r][c-1] == "1":
                            flag = 0
                            break
                    if flag:
                        col = tuple([(r, c-1) for r, c in newTemp])
                        checkVisited(col, 0, cnt)

                # R
                elif cmd == 3:
                    flag = 1
                    for r, c in newTemp:
                        if not (0 <= c+1 < N) or plain[r][c+1] == "1":
                            flag = 0
                            break
                    if flag:
                        col = tuple([(r, c+1) for r, c in newTemp])
                        checkVisited(col, 0, cnt)

                # T
                else:
                    flag = 1
                    for r, c in newTemp:
                        if not (1 <= c < N-1):
                            flag = 0
                            break
                        if plain[r][c-1] == "1" or plain[r][c+1] == "1":
                            flag = 0
                            break
                    if flag:
                        cr, cc = newTemp[1] 
                        row = ((cr, cc-1), (cr, cc), (cr, cc+1))
                        checkVisited(row, 1, cnt)

        else:
            for cmd in range(5):
                # U
                if cmd == 0:
                    flag = 1
                    for r, c in newTemp:
                        if not (0 <= r-1 < N) or plain[r-1][c] == "1":
                            flag = 0
                            break
                    if flag:
                        row = tuple([(r-1, c) for r, c in newTemp])
                        checkVisited(row, 1, cnt)

                # D
                elif cmd == 1:
                    flag = 1
                    for r, c in newTemp:
                        if not (0 <= r+1 < N) or plain[r+1][c] == "1":
                            flag = 0
                            break
                    if flag:
                        row = tuple([(r+1, c) for r, c in newTemp])
                        checkVisited(row, 1, cnt)

                # L
                elif cmd == 2:
                    row = deque(newTemp)
                    r, c = row[0]
                    if (0 <= c-1 < N) and plain[r][c-1] == "0":
                        row.pop()
                        row.appendleft((r, c-1))
                        checkVisited(tuple(row), 1, cnt)

                # R
                elif cmd == 3:
                    row = deque(newTemp)
                    r, c = row[-1]
                    if (0 <= c+1 < N) and plain[r][c+1] == "0":
                        row.popleft()
                        row.append((r, c+1))
                        checkVisited(tuple(row), 1, cnt)

                # T
                else:
                    flag = 1
                    for r, c in newTemp:
                        if not (1 <= r < N-1):
                            flag = 0
                            break
                        if plain[r+1][c] == "1" or plain[r-1][c] == "1":
                            flag = 0
                            break
                    if flag:
                        cr, cc = newTemp[1]
                        col = ((cr-1, cc), (cr, cc), (cr+1, cc))
                        checkVisited(col, 0, cnt)
    return 0

N = int(input())
start, goal = [], [] 
plain = []
for r in range(N):
    plain.append(list(input().rstrip()))
    for c in range(N):
        if plain[r][c] == "B":
            start.append((r, c))
            plain[r][c] = "0"
        elif plain[r][c] == "E":
            goal.append((r, c))
            plain[r][c] = "0"

startDir = checkDir(start) 
goal = tuple(goal)
 
visited = set()         
visited.add(tuple(start))   
q = deque([(start, startDir, 0)])     

print(bfs())