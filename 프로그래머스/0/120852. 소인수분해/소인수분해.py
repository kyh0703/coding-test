def solution(n):
    answer = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            answer.append(d)
            n //= d
        d += 1
    if n > 1:
        answer.append(n)
        
    answer = sorted(list(set(answer)))
    return answer