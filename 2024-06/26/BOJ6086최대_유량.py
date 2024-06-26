import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graphs = {}
counts=[[0 for j in range(52)] for i in range(52)]
flow=[[0 for j in range(52)] for i in range(52)]
maxFlow=0
end=ord('Z')-ord('A')

def AlphaToNum(alpha):
    if ord(alpha) > ord('Z'):
        return ord(alpha) - ord('a') + 26
    else:
        return ord(alpha) - ord('A')

def findMinWeight(node):
    global minFlow
    
    if node == 0:
        return 
    
    rest = counts[prev[node]][node] - flow[prev[node]][node]
    if rest < minFlow:
        minFlow = rest
    findMinWeight(prev[node])

def makeFlow(node):
    if node == 0:
        return
    flow[prev[node]][node] += minFlow
    flow[node][prev[node]] -= minFlow
    makeFlow(prev[node])

for i in range(52):
    graphs[i]=[]

for _ in range(n):
    a,b,cost=input().split()
    numA=AlphaToNum(a)
    numB=AlphaToNum(b)
    cost=int(cost)

    counts[numA][numB] += cost
    counts[numB][numA] += cost
    graphs[numA].append(numB)
    graphs[numB].append(numA)

while True:
    prev = [-1 for i in range(52)]
    q = deque()
    q.append(0)
    while q:
        node = q.popleft()
        if node == end:
            break
        for nextNode in graphs[node]:
            if prev[nextNode] == -1 and counts[node][nextNode] > flow[node][nextNode]:
                q.append(nextNode)
                prev[nextNode] = node
                
    if prev[end] == -1:
        break
    minFlow = sys.maxsize
    findMinWeight(end)
    makeFlow(end)
    maxFlow += minFlow

print(maxFlow)