def solution(want, number, discount):
    answer = 0
    dict = {}
    for i in range(len(want)):
        dict[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        temp = dict.copy()
        for j in range(i, i+10):
            if discount[j] in temp:
                temp[discount[j]] -= 1
                if temp[discount[j]] == 0:
                    temp.pop(discount[j],None)
        if temp == {}:
            answer += 1
    return answer