n,m = map(int,input().split())
parks = list(map(int,input().split()))

if m >= n:
    print(n)
else:
    start = 0
    end = 20000000000000000000
    total = 0
    while start <= end:
        mid = (start+end)//2
        flag = False
        cnt = m
        for t in parks:
            cnt += mid//t
            if cnt >= n:
                flag = True
        if flag:
            total = mid
            end = mid - 1
        else:
            start = mid + 1

    person = m
    for t in parks:
        person += (total-1)//t

    for idx,t in enumerate(parks,1):
        if total % t == 0:
            person += 1
        if person == n:
            print(idx)
            break