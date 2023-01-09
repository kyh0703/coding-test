N = int(input())
answer = [input() for _ in range(N)]
answer_dict = dict()
for i in answer:
    answer_dict[i] = answer_dict.get(i, 0) + 1
v, _ = max(answer_dict.items(), key=lambda item: item[1])
print('Junhee is not cute!' if v == '0' else 'Junhee is cute!')
