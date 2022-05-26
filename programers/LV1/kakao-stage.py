def solution(N, stages):
    answer = []
    stages_dict = dict()
    calculate_dict = dict()
    for stage in stages:
        stages_dict[stage] = stages_dict.get(stage, 0) + 1

    for n in range(1, N + 1):
        removes = []
        stop = 0
        total = sum(stages_dict.values())
        for stage, count in stages_dict.items():
            if stage <= n:
                stop += count
                removes.append(stage)
        for remove in removes:
            stages_dict.pop(remove)
        if stop == 0 and total == 0:
            calculate_dict[n] = 0
        else:
            calculate_dict[n] = stop/(total)

    calculate_dict = sorted(calculate_dict.items(),
                            key=lambda x: x[1], reverse=True)
    for key, _ in calculate_dict:
        answer.append(key)

    return answer


print("answer: ", solution(5, [2, 2, 2, 2, 2]))
# , [3, 4, 2, 1, 5]
"""
입출력 예 #1
1번 스테이지에는 총 8명의 사용자가 도전했으며, 이 중 1명의 사용자가 아직 클리어하지 못했다. 따라서 1번 스테이지의 실패율은 다음과 같다.

1 번 스테이지 실패율 : 1/8
2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했다. 따라서 2번 스테이지의 실패율은 다음과 같다.

2 번 스테이지 실패율 : 3/7
마찬가지로 나머지 스테이지의 실패율은 다음과 같다.

3 번 스테이지 실패율 : 2/4
4번 스테이지 실패율 : 1/2
5번 스테이지 실패율 : 0/1
각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같다.

[3,4,2,1,5]
입출력 예 #2

모든 사용자가 마지막 스테이지에 있으므로 4번 스테이지의 실패율은 1이며 나머지 스테이지의 실패율은 0이다.

[4,1,2,3] """
