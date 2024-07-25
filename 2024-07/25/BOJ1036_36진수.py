import sys
from collections import deque

input = sys.stdin.readline

toConvert = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(num):
    if num == 0:
        return '0'
    q = deque()
    while num:
        q.appendleft(toConvert[num%36])
        num //= 36
    return ''.join(q)


n = int(input())

totalSum = 0
diff = [0]*36

for _ in range(n):
    num = input().strip()
    totalSum += int(num,36)
    length = len(num)
    for i in range(length):
        tmp = int(num[length-i-1],36)
        diff[tmp] += (35-tmp)*(36**i)

diff.sort(reverse=True)
k = int(input())

for i in range(k):
    totalSum += diff[i]

print(convert(totalSum))