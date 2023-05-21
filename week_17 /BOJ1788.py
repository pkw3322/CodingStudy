n = int(input())
arr = [0,1]
for i in range(2,abs(n)+1):
    arr.append((arr[i-1]+arr[i-2])%1000000000)

if n == 0 : 
    print(0)
elif n%2 == 0 and n < 0:
    print(-1)
else : 
    print(1)

print(arr[abs(n)])