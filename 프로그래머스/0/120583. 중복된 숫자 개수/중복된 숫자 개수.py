from collections import Counter

def solution(array, n):
    d = Counter(array)
    return d[n]