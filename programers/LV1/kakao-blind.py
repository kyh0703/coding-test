def solution(id_list, report, k):
    answer = [0] * len(id_list)
    id_dict = {key: i for i, key in enumerate(id_list)}
    #  신고 당한 사람
    report_dict = dict.fromkeys(report, 0)
    receive_dict = dict()
    stop_dict = dict()
    for r in report_dict:
        reporter, receiver = r.split()
        count = receive_dict.get(receiver)
        sum = 1 if count == None else count + 1
        receive_dict[receiver] = sum
        if k <= sum:
            stop_dict[receiver] = sum

    # 신고한 사람
    for r in report_dict:
        reporter, receiver = r.split()
        if receiver in stop_dict:
            index = id_dict[reporter]
            answer[index] += 1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# 이건데.. 제길..
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer