import math

score_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

scores = 0.0
answer = []
for _ in range(20):
    name, score, degree = map(str, input().split())
    if degree == 'P':
        continue
    answer.append(float(score) * float(score_dict[degree]))
    scores += float(score)
print(f"{sum(answer) / scores:.6f}")
