import sys

input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    todoList = input().rstrip()

    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    if n == 0:
        arr = []

    backFlag = False # R 개수가 짝수면 False, 홀수면 True
    errorFlag = False # arr length보다 D가 더 많으면 error 출력하게 되는데 이때 확인하기 위한 Flag

    for i in todoList:
        if i == 'R':
            backFlag = not backFlag
        elif i == 'D':
            if len(arr) == 0 or n == 0:
                print('error')
                errorFlag = True
                break
            if backFlag:
                arr.pop()
            else:
                arr.pop(0)
            n -= 1
            
    # 여기서 원래 len(arr) != 0으로 확인 했었는데,
    #  깔끔하게 지워지는 경우 len(arr) = 0일 수도 있음. 
    # 따라서 errorFlag를 추가하여 해결
    if not errorFlag:  
        if backFlag:
            arr = arr[::-1]
        print ('[' + ','.join(arr) + ']')
