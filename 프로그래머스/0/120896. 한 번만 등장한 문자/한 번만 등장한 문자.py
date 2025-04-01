def solution(s):
    return ''.join(sorted([ch for ch in s if s.count(ch) == 1]))
