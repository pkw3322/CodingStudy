import sys

input = sys.stdin.readline

def dfs(picks):
    if len(picks) == n:
        for num in mustInclude:
            if num not in picks:
                return 0
        return 1
    ret = 0
    for i in range(10):
        picks.append(i)
        ret += dfs(picks)
        picks.pop()
    return ret

n,m = map(int,input().split())
mustInclude = list(map(int,input().split())) if m != 0 else []

ans = dfs([])

print(ans)