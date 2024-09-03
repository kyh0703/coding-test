def solution(a, d, included):
    answer = 0
    temp = a
    for i in included:
        if i == True:
            answer += temp
        temp += d
    return answer