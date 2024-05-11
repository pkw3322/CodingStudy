import sys

input = sys.stdin.readline

n = int(input())
costs = [0]
preBuild = [[]]

for i in range(1,n+1):
    lines = list(map(int, input().split()))
    costs.append(lines[0])
    toAppend = []
    for j in range(1,len(lines)):
        if lines[j] == -1:
            continue
        toAppend.append(lines[j])
    preBuild.append(toAppend)

visited = [False for _ in range(n+1)]

def check():
    for i in range(1,n+1):
        if not visited[i]:
            return False
    return True

for i in range(1,n+1):
    if not preBuild[i]:
        visited[i] = True
        continue

while not check():
    for i in range(1,n+1):
        if visited[i]:
            continue
        flag = True
        for j in preBuild[i]:
            if not visited[j]:
                flag = False
                break
        if flag:
            visited[i] = True
            costs[i] = max([costs[j] for j in preBuild[i]]) + costs[i]
    

for i in costs[1:]:
    print(i)