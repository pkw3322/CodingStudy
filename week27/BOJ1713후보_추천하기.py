import sys
input = sys.stdin.readline

n = int(input())
count = int(input())

arr = list(map(int,input().split()))

pictures = []
scores = []

for i in range(count):
    if arr[i] in pictures:
        for j in range(len(pictures)):
            if arr[i] == pictures[j]:
                scores[j] += 1
    else:
        if len(pictures) >= n:
            for j in range(n):
                if scores[j] == min(scores):
                    pictures.pop(j)
                    scores.pop(j)
                    break
        pictures.append(arr[i])
        scores.append(1)
pictures.sort()
print(' '.join(map(str,pictures)))