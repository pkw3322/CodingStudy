import sys

input = sys.stdin.readline

string = input().rstrip()

def check(s):
    return s != '(' and s != ')' and s != ''

def getCount(s):
    if s == '':
        return 0
    ret = 0
    inpu = []
    stack = []
    before = ''
    multi = 0
    isAppend = False
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            if not isAppend:
                isAppend = True
                multi = int(before)
                before = s[i]
                continue
        elif s[i] == ')':
            stack.pop()
            if stack == []:
                isAppend = False
                ret += multi * getCount(''.join(inpu))
                inpu = []
                before = s[i]
                continue
        if isAppend:
            inpu.append(s[i])
        if not isAppend and check(s[i]) and check(before): 
            ret += 1
        before = s[i]
    if check(before):
        ret += 1
    return ret

print(getCount(string))