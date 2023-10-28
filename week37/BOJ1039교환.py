from collections import deque

m,k = map(int, input().split())

size = len(str(m))


def bfs():
    ans = 0
    visited = set()
    visited.add((m, 0))
    q = deque()
    q.append((m, 0))
    while q:
        cur,cnt = q.popleft()
        if cnt == k:
            ans = max(ans,cur)
            continue
        arr = list(str(cur))
        for i in range(size-1):
            for j in range(i+1,size):
                if i == 0 and arr[j] == '0': 
                    continue
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                num = int(''.join(arr))
                if (num,cnt+1) not in visited:
                    q.append((num,cnt+1))
                    visited.add((num,cnt+1))
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return ans if ans else -1

print(bfs())