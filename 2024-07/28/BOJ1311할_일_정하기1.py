import sys

input = sys.stdin.readline

n = int(input())

works = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1]*(1<<n) for _ in range(n)]

def findMin(row, state):
    if row == n:
        return 0
    if visited[row][state] != -1:
        return visited[row][state]
    visited[row][state] = int(1e9)
    for i in range(n):
        if state & (1<<i):
            continue
        visited[row][state] = min(visited[row][state], findMin(row+1, state | (1<<i)) + works[row][i])

    return visited[row][state]

print(findMin(0,0))