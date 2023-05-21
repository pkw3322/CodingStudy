import sys

n = int(sys.stdin.readline())

pos = []
neg = []
maxSum = 0

for _ in range(n):
    a = int(sys.stdin.readline())

    if a < 1:
        neg.append(a)
    elif a == 1:
        maxSum += 1
    else :
        pos.append(a)

pos.sort(reverse=True)
neg.sort()

if len(pos)%2 == 0:
    for i in range(0,len(pos),2):
        maxSum += (pos[i]*pos[i+1])
else:
    for i in range(0,len(pos)-1,2):
        maxSum += (pos[i]*pos[i+1])
    maxSum += pos[-1]

if len(neg)%2 == 0:
    for i in range(0,len(neg),2):
        maxSum += (neg[i]*neg[i+1])
else:
    for i in range(0,len(neg)-1,2):
        maxSum += (neg[i]*neg[i+1])
    maxSum += neg[-1]

print(maxSum)