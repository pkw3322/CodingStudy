import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input().rstrip())*10000000
        n = int(input())
        sticks = [int(input()) for _ in range(n)]
        sticks.sort()
        left,right = 0,n-1
        res = []
        while left < right:
            if sticks[left] + sticks[right] == x:
                res = [sticks[left],sticks[right]]
                break
            elif sticks[left] + sticks[right] < x:
                left += 1
            else:
                right -= 1
        if res:
            print(f'yes {res[0]} {res[1]}')
        else:
            print('danger')
    except:
        break