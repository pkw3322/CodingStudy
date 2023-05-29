import sys

s = []
ans = ''
str = input()


for c in str:
    if c in ['+','-','*','/','(',')']:
        if c == '(':
            s.append(c)
        elif c == ')':
            while s and s[-1] != '(':
                ans += s.pop()
            s.pop()
        elif c == '*' or c == '/':
            while s:
                if s[-1] != '*' and s[-1] != '/':
                    break
                ans += s.pop()
            s.append(c)
        elif c == '+' or c == '-':
            while s and s[-1] != '(':
                ans += s.pop()
            s.append(c)
    else :
        ans += c
while s:
    ans += s.pop()

print(ans)
