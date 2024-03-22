n = int(input())


def star(n):
    if n == 3:
        return ['***', '* *', '***']
    else:
        temp = star(n//3)
        result = []
        for i in range(n):
            if i // (n//3) == 1:
                result.append(temp[i % (n//3)] + ' ' * (n//3) + temp[i % (n//3)])
            else:
                result.append(temp[i % (n//3)] * 3)
        return result

print('\n'.join(star(n)))