import re

testCase = int(input())
for i in range(testCase):
    a = input()
    reP = re.compile('(100+1+|01)+')
    if reP.fullmatch(a):
        print("YES")
    else : 
        print("NO")