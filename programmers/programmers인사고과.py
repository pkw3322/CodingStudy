def solution(scores):
    answer = 1
    a,b = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    c = 0
    for i,j in scores:
        if a < i and b < j:
            return -1
        if c <= j:
            if a+b < i+j:
                answer += 1
            c = j
    return answer
