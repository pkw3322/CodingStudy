import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
l = [0]

for tem in arr:
    if l[-1] < tem:
        l.append(tem)
    else:
        start,end = 0,len(l)
        while start < end:
            mid = (start + end)//2
            if l[mid] < tem:
                start = mid + 1
            else :
                end = mid

        l[end] = tem

print(len(l)-1)