items = [list(map(int, input().split())) for _ in range(3)]
answer = []
for item in items:
    count_dict = dict()
    for i in item:
        count_dict[i] = count_dict.get(i, 0) + 1

    zero_count = count_dict.get(0, 0)
    if zero_count == 1:
        answer.append('A')
    elif zero_count == 2:
        answer.append('B')
    elif zero_count == 3:
        answer.append('C')
    elif zero_count == 4:
        answer.append('D')
    else:
        answer.append('E')

for i in answer:
    print(i)