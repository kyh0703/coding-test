import sys
import math

def round_half_up(n):
    return int(math.floor(n + 0.5))

input = sys.stdin.readline
N = int(input())
input_scores = []
for _ in range(N):
    input_scores.append(int(input()))
input_scores.sort()
except_cnt = round_half_up(N*0.15)
if except_cnt == 0:
    scores = input_scores
else:
    scores = input_scores[except_cnt:-except_cnt]
answer = 0 if len(scores) == 0 else round_half_up(sum(scores) / len(scores))
print(answer)
