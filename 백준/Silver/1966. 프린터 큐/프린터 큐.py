from collections import deque

for _ in range(int(input())):
    N, K = map(int, input().split())
    doc = deque(map(int, input().split()))
    index = deque(range(len(doc)))
    answer = 0
    while doc:
        i, v = index[0], doc[0]
        if v < max(doc):
            doc.append(doc.popleft())
            index.append(index.popleft())
        else:
            if v == max(doc):
                doc.popleft()
                index.popleft()
                answer += 1
            if i == K:
                break
    print(answer)