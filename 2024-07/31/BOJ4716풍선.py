import sys

input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    if n == 0 and a == 0 and b == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.sort(key=lambda x: abs(x[1] - x[2]), reverse=True)
    totalDist = 0
    equalDist = []

    for k,da, db in arr:
        if da > db:
            if b >= k:
                totalDist += db*k
                b -= k
            else:
                totalDist += db*b
                k -= b
                b = 0
                totalDist += da*k
        elif da < db:
            if a >= k:
                totalDist += da*k
                a -= k
            else:
                totalDist += da*a
                k -= a
                a = 0
                totalDist += db*k
        else:
            equalDist.append([k, da])
    

    for i in range(len(equalDist)):
        totalDist += equalDist[i][0]*equalDist[i][1]

    print(totalDist)