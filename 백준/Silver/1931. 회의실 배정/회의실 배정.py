N = int(input())
conf_info = [list(map(int, input().split())) for _ in range(N)]
conf_info.sort(key=lambda x: x[0])
conf_info.sort(key=lambda x: x[1])

end_time = 0
answer = 0
for s, e in conf_info:
    if end_time <= s:
        end_time = e
        answer += 1
print(answer)