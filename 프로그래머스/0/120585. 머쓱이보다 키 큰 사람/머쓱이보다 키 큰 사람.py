def solution(array, height):
    answer = 0
    sorted_array = sorted(array, reverse=True)
    for i in sorted_array:
        if i > height:
            answer += 1
    return answer