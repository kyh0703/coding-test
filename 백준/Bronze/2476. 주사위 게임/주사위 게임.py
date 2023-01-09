N = int(input())
answer = 0
for _ in range(N):
    scores = list(map(int, input().split()))
    score_dict = dict()
    for i in scores:
        score_dict[i] = score_dict.get(i, 0) + 1

    money = 0
    max_score, max_count = max(score_dict.items(), key=lambda item: item[1])
    if max_count == 1:
        max_score, _ = max(score_dict.items(), key=lambda item: item[0])
        money = max_score * 100
    elif max_count == 2:
        money = 1_000 + max_score * 100
    elif max_count == 3:
        money = 10_000 + max_score * 1_000

    if answer < money:
        answer = money

print(answer)
