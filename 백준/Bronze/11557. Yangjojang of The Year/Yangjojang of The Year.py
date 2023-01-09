T = int(input())
for _ in range(T):
    N = int(input())
    first_school = ''
    max_alcohol = 0
    for i in range(N):
        school, alcohol = map(str, input().split())
        if max_alcohol < int(alcohol):
            max_alcohol = int(alcohol)
            first_school = school
    print(first_school)
