def solution(sides):
    answer = set()
    sides.sort(reverse=True)
    one, two = sides
    for i in range(1, one + 1):
        if i + two > one:
            answer.add(i)
    for i in range(one, one+two):
        answer.add(i)
    return len(answer)