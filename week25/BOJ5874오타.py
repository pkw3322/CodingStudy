arr = list(input())

res = 0
left,right,total = 0,0,0

for i in range(len(arr)):
    if arr[i] == '(':
        left += 1
        total += 1
    else:
        right += 1
        total -= 1
        
    if total == 1:
        left = 0
    if total == -1:
        res = right
        break
if total == 2:
    res = left

print(res)