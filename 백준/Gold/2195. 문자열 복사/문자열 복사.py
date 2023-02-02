S = input()
P = input()
answer = 0

while len(P) != 0:
    for i in range(len(P), 0, -1):
        if P[:i] in S:
            P = P[i:]
            answer += 1
            break

print(answer)