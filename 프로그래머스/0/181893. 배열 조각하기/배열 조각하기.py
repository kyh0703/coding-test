def solution(arr, query):
    answer = arr.copy()
    for i, v in enumerate(query):
        if i % 2 == 0:
            answer = answer[:v+1]
        else:
            answer = answer[v:]
    return answer