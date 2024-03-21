from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

puzzle = ""
for _ in range(3):
    puzzle += "".join(list(input().split()))

distance = dict()

distance[puzzle] = 0

def bfs():
    q = deque()
    q.append(puzzle)
    while q:
        cur = q.popleft()
        if cur == "123456780":
            return distance[cur]
        idx = cur.find("0")
        x, y = idx // 3, idx % 3
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                nidx = nx * 3 + ny
                ncur = list(cur)
                ncur[idx], ncur[nidx] = ncur[nidx], ncur[idx]
                ncur = "".join(ncur)
                if ncur not in distance:
                    distance[ncur] = distance[cur] + 1
                    q.append(ncur)
    return -1

print(bfs())
