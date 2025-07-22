words = []
for _ in range(5):
    words.append(list(map(str, input())))

answer =""
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            answer += words[j][i]
print(answer)
