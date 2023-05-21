import sys
N,r,c = map(int,input().split())

ans = 0

def search(x,y,n):
    global ans
    if x > r or x + n <= r or y > c or y + n <= c:
        ans += n**2
        return
    if n > 2:
        n = n//2
        search(x,y,n)
        search(x,y+n,n)
        search(x+n,y,n)
        search(x+n,y+n,n)
    else:
        if x==r and y == c:
            print(ans)
        elif x==r and y+1 == c:
            print(ans+1)
        elif x+1 == r and y == c:
            print(ans+2)
        else :
            print(ans+3)
        sys.exit()

search(0,0,2**N)