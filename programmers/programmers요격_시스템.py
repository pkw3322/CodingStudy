def solution(targets):
    answer = 0
    targets.sort(key= lambda x: [x[1],x[0]])
    s = 0
    e = 0
    for ts,te in targets:
        if ts >= e:
            answer += 1
            e = te

    return answer 