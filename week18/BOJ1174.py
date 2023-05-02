import sys

arr = list()
result = set()

def func():
    if len(arr) > 0:
        result.add(int("".join(map(str,arr))))

    for i in range(0, 10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            func()
            arr.pop()

N = int(sys.stdin.readline())

try:
    func()
    result = list(result)
    result.sort()
    print(result[N-1])
except:
    print(-1)