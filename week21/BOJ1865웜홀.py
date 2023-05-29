import sys

input = sys.stdin.readline

def fun(start):
    dist[start] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for next,t in edges[j]:
                if dist[next] > dist[j] + t:
                    dist[next] = dist[j] + t
                    if i == n:
                        return True
    return False

t = int(input())
for _ in range(t):
    n,m,w = map(int,input().split())
    edges = [[] for _ in range(n+1)]
    dist = [10001 for _ in range(n+1)]

    for _ in range(m):
        s,e,t = map(int,input().split())
        edges[s].append([e,t])
        edges[e].append([s,t])
    for _ in range(w):
        s,e,t = map(int,input().split())
        edges[s].append([e,-t])
    
    ans = fun(1)
    if not ans:
        print("NO")
    else:
        print("YES") 
