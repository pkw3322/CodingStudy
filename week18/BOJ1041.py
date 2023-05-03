n = int(input())
arr = list(map(int,input().split()))

sumList = list()
ans = 0
if n == 1 : 
    ans = sum(arr) - max(arr)

else : 
    sumList = [min(arr[0],arr[5]),
               min(arr[1],arr[4]),
               min(arr[2],arr[3])]
    sumList.sort()

    n1 = (n-2)*(n-2) + (n-1)*(n-2)*4
    n2 = (n-2)*4 + (n-1)*4
    n3 = 4
    ans = n1*sumList[0] + n2*sum(sumList[:2]) + n3*sum(sumList)

print(ans)