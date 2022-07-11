def GCD(a, b):
    r = a % b
    if r == 0:
        return b
    return GCD(b, r)


def LCM(a, b):
    return (a * b) // GCD(a, b)


def solution(arr):
    arr.sort()
    answer = arr[0]
    for i in range(1, len(arr)):
        a, b = answer, arr[i]
        answer = LCM(a, b)
    return answer