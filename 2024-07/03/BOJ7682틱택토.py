import sys

input = sys.stdin.readline

def checkGameEnd(case,typ):
    if case[0] == typ and case[0] == case[1] == case[2]:
        return True
    elif case[0] == typ and case[0] == case[3] == case[6]:
        return True
    elif case[0] == typ and case[0] == case[4] == case[8]:
        return True
    elif case[1] == typ and case[1] == case[4] == case[7]:
        return True
    elif case[2] == typ and case[2] == case[5] == case[8]:
        return True
    elif case[2] == typ and case[2] == case[4] == case[6]:
        return True
    elif case[3] == typ and case[3] == case[4] == case[5]:
        return True
    elif case[6] == typ and case[6] == case[7] == case[8]:
        return True
    else:
        return False

while True:
    case = input().strip()
    if case == 'end':
        break
    xCnt = case.count('X')
    oCnt = case.count('O')

    if xCnt == oCnt+1 or xCnt == oCnt:
        typ1,typ2 = ('X','O') if xCnt == oCnt+1 else ('O','X')
        res1 = checkGameEnd(case, typ1)
        res2 = checkGameEnd(case, typ2)

        if res2:
            print('invalid')
        elif not res1:
            if case.count('.') == 0:
                print('valid')
            else:
                print('invalid')
        else:
            print('valid')
    else:
        print('invalid')
