def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    top, middle, low  = sides
    print(top, middle, low)
    return 1 if top < middle + low else 2