strs = list(input())

strs = list(filter((' ').__ne__, strs))
str2 = []

case = int(input())


for _ in range(case):
    a = input()
    if a[0] == 'P':
        strs.append(a[2])
    elif a[0] == 'L':
        if strs:
           str2.append(strs.pop()) 
    elif a[0] == 'D':
        if str2:
            strs.append(str2.pop())
    else :
        if strs:
            strs.pop()
strs.extend(reversed(str2))
print(''.join(strs))